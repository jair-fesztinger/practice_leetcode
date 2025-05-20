import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    mega = (world['population'] >= 25000000) | (world['area'] >= 3000000)

    return world.loc[mega, ['name', 'population', 'area']]