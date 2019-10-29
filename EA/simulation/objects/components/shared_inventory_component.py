import weakref
class SharedInventoryComponent(InventoryComponent, component_name=types.INVENTORY_COMPONENT):

    def __init__(self, owner, inventory_type):
        super().__init__(owner)
        self._inventory_type = inventory_type
        self._storage = InventoryStorage(self.inventory_type, self.default_item_location, max_size=InventoryTypeTuning.get_max_inventory_size_for_inventory_type(self.inventory_type))
        self._hidden_storage = InventoryStorage(self.inventory_type, self.default_item_location, allow_ui=False, hidden_storage=True)

    @property
    def inventory_type(self):
        return self._inventory_type

    @property
    def default_item_location(self):
        return ItemLocation.OBJECT_INVENTORY

    @componentmethod
    def get_inventory_access_constraint(self, *args, **kwargs):
        constraint_list = []
        for obj in self.owning_objects_gen():
            constraint_list.append(obj.get_inventory_access_constraint(*args, **kwargs))
        return create_constraint_set(constraint_list, debug_name='Object Inventory Constraints')

    @componentmethod
    def get_inventory_access_animation(self, *args, **kwargs):
        for obj in self.owning_objects_gen():
            return obj.get_inventory_access_animation(*args, **kwargs)

    def _get_inventory_object(self):
        pass

class SharedInventoryContainer(ComponentContainer):

    def __init__(self, inventory_type):
        super().__init__()
        self.add_component(SharedInventoryComponent(self, inventory_type))
        self.id = 1

    @constproperty
    def is_sim():
        return False

    def ref(self, callback=None):
        return weakref.ref(self, callback)
