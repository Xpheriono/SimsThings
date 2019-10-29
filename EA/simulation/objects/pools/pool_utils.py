from _weakrefset import WeakSet
    cached_pool_objects = WeakSet()
def get_main_pool_objects_gen():
    yield from cached_pool_objects

def get_pool_by_block_id(block_id):
    for pool in get_main_pool_objects_gen():
        if pool.block_id == block_id:
            return pool
    zone = services.current_zone()
    if zone is not None and not services.current_zone().is_in_build_buy:
        logger.error('No Pool Matching block Id: {}', block_id, owner='camilogarcia')
