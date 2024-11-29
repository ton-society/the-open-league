from models.project import DeFi

SwapCoffeeTVL = DeFi(
    name="swap.coffee",
    defillama_slug="swap.coffee",
    url="https://swap.coffee/stake",
    chain='TON-staking'
)


SwapCoffeeVolume = DeFi(
    name="swap.coffee",
    defillama_slug="swap.coffee",
    url="https://swap.coffee/dex",
    category="aggregators",
)
