
currentWorkingDirectory = "D:\\Masters\\1st Semester\\Advanced SE\\Advanced-SE---Project-1"

# -----------------------------------------------------------------------------
import os
os.chdir(currentWorkingDirectory)
print("Current working directory\n" + os.getcwd())

import pandas                        as pd
from core import methods             as m1
from core import HelperTools         as ht

from config                          import pdict

# -----------------------------------------------------------------------------
@ht.timer
def main():
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""

    df_geodat_plz   = pd.read_csv(pdict["file_geodat_plz"] , delimiter = ';')

    df_lstat        = pd.read_csv(pdict["file_lstations"])
    df_lstat2       = m1.preprop_lstat(df_lstat, df_geodat_plz, pdict)
    gdf_lstat3      = m1.count_plz_occurrences(df_lstat2)
    
    df_residents    = pd.read_csv(pdict["file_residents"])
    gdf_residents2  = m1.preprop_resid(df_residents, df_geodat_plz, pdict)
    
    m1.make_streamlit_electric_Charging_resid(gdf_lstat3, gdf_residents2)
# -----------------------------------------------------------------------------------------------------------------------

    #


if __name__ == "__main__": 
    main()

