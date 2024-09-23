from models.metric import Metric, CalculationContext, RedoubtMetricImpl, ToncenterCppMetricImpl


class SmartContractInteractionRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        if len(metric.op_codes) > 0:
            op_codes_filter = " OR ".join(map(lambda op: f"op = {op}", metric.op_codes))
        else:
            op_codes_filter = "TRUE"
        if metric.comment_regexp:
            comment_regexp_filter = f"and comment like '{metric.comment_regexp}'"
        else:
            comment_regexp_filter = ""
        if metric.address:
            address_filter = f"destination ='{metric.address}'"
        else:
            assert len(metric.addresses) > 0, f"You should provide either address or addresses non empty list " \
                                              f"({context.project.name}: {metric.description})"
            address_filter = " OR ".join(map(lambda a: f"destination ='{a}'", metric.addresses))
        if len(metric.comment_not_equals) > 0:
            comment_not_equals_filter = "and " + " and ".join(map(lambda v: f"comment != '{v}'", metric.comment_not_equals))
        else:
            comment_not_equals_filter = ""
        return f"""
        select 
                msg_id as id, '{context.project.name}' as project, {0.5 if metric.is_custodial else 1} as weight, 
                source as user_address, ts from messages_local m
        where ({address_filter}) {'and length("comment") > 0' if metric.comment_required else ''}
         {comment_regexp_filter} {comment_not_equals_filter}
        AND (
            {op_codes_filter}
        )
        """


class SmartContractInteractionToncenterCppImpl(ToncenterCppMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        if len(metric.op_codes) > 0:
            op_codes_filter = " OR ".join(map(lambda op: f"opcode = {op}", metric.op_codes))
        else:
            op_codes_filter = "TRUE"
        if metric.comment_regexp:
            comment_regexp_filter = f"and comment like '{metric.comment_regexp}'"
        else:
            comment_regexp_filter = ""
        if metric.address:
            address_filter = f"t.account ='{self.to_raw(metric.address)}'"
        else:
            assert len(metric.addresses) > 0, f"You should provide either address or addresses non empty list " \
                                              f"({context.project.name}: {metric.description})"
            address_filter = " OR ".join(map(lambda a: f"t.account ='{self.to_raw(a)}'", metric.addresses))
        if len(metric.comment_not_equals) > 0:
            comment_not_equals_filter = "and " + " and ".join(map(lambda v: f"comment != '{v}'", metric.comment_not_equals))
        else:
            comment_not_equals_filter = ""

        return f"""
        select 
                t.hash as id, '{context.project.name}' as project,
                source as user_address, t.now as ts from transactions t
                join messages m on m.tx_hash = t.hash and direction = 'in'
                -- TODO replace left join to inner join for comment_required case
                left join parsed.message_comments mc on mc.hash = m.body_hash
        where compute_exit_code = 0 and action_result_code = 0 and 
            now >= {context.season.start_time}::integer and
                now < {context.season.end_time}::integer and
        ({address_filter}) {'and length("comment") > 0' if metric.comment_required else ''}
         {comment_regexp_filter} {comment_not_equals_filter}
        AND (
            {op_codes_filter}
        )

        """


"""
Simple smart contract interaction - any message (but resulted in successful transaction) to the address provided
Options:
* address - single address
* addresses - list of addresses
* is_custodial - custodial flag
* comment_required - comment required flag
* op_codes - list of op codes (please use signed decimal notation, not hex!)
* comment_regexp - comment regexp to filter with
* comment_not_equals - list of strings from comment to exclude  
"""
class SmartContractInteraction(Metric):
    def __init__(self, description, address=None, addresses=[], is_custodial=False,
                 comment_required=False, op_codes=[], comment_regexp=None, comment_not_equals=[]):
        Metric.__init__(self, description, [SmartContractInteractionRedoubtImpl(), SmartContractInteractionToncenterCppImpl()])
        assert type(addresses) == list
        assert type(op_codes) == list
        self.address = address
        self.addresses = addresses
        self.is_custodial = is_custodial
        self.comment_required = comment_required
        self.op_codes = op_codes
        self.comment_regexp = comment_regexp
        self.comment_not_equals = comment_not_equals

