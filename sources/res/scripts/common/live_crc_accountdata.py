from __future__ import absolute_import
from live_crc import gen_delSubkeys_fn, gen_livehash_fn, gen_mergeCache_fn, gen_extract_fn, INCLUDE
accountPersistentCacheDataScheme = {INCLUDE: {
           3, 4, 5, 6, 7, 8}, 
   b'stats': {INCLUDE: {
                      b'dossier', b'eliteVehicles', b'unlocks', b'vehTypeXP'}}}
accountDataPersistentHash = gen_livehash_fn(accountPersistentCacheDataScheme)
accountDataDelPersistent = gen_delSubkeys_fn(accountPersistentCacheDataScheme)
accountDataMergePersistent = gen_mergeCache_fn(overwrite=False)
accountDataExtractPersistent = gen_extract_fn(accountPersistentCacheDataScheme)

def accountDataGetDiffForPersistent(diff):
    good_keys = {
     1, 2, 3, 4, 5, 6, 7}
    mydiff = {}
    for k, v in diff.items():
        if k in good_keys or isinstance(k, tuple) and k[0] in good_keys:
            mydiff[k] = v

    return mydiff
