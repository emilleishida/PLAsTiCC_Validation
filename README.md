# PLAsTiCC_Validation
Validation exercises for PLAsTiCC


Check [example notebook for MODEL01](https://github.com/emilleishida/PLAsTiCC_Validation/blob/master/pkl/MODEL01/PLAsTiCC_validation_MODEL01.ipynb)


## Current Validation tasks


**Emille** - MODEL01

**Kara** - MODEL03

**Mi** - 

**Renee** - MODEL50

**Rafael** - MODEL80

---

### `validutils`

Set of tools for interacting with the supernovae simulations.

#### Scripts

* **`serialize_lsst_model.py`**

    Takes as input a directory containing a run of simulations (e.g. `LSST_DDF_MODEL45`) and returns a compressed dictionary (`LSST_DDF_MODEL45.pkl.gz` file) of supernovae data index by their ID. 

    **Usage:**
    ```bash
    python serialize_lsst_model.py <LSST_sim_dir>  # output file in current dir
    python serialize_lsst_model.py <LSST_sim_dir> --destination=<output_dir>      python serialize_lsst_model.py --help  # for help
    ```
