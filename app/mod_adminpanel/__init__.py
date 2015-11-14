from importlib import import_module


def setup_module(app, nav):
    setup_navigation(app, nav)


# Sets up a navigation menu item for each module with mod_adminpanel integration.
def setup_navigation(app, nav):
    items_to_add = []
    for name, blueprint in app.blueprints.items():
        module = import_module(blueprint.import_name)
        # Check if blueprint has a form named ConfigForm.
        # Check if blueprint has a function named do_config_form_logic.
        # If both of those are implemented then the module should have an adminpanel page.
        try:
            module.ConfigForm
            module.do_config_form_logic
        except AttributeError as e:
            continue
        items_to_add.append(name)

    # Create navigation bar
    items = [nav.Item(x, 'adminpanel.configure_module', {'bp_name': x}) for x in items_to_add]
    nav.Bar('adminpanel', items)