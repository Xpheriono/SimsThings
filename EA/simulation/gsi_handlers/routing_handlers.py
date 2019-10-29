import traceback
    sub_schema.add_field('index', label='Index', type=GsiFieldVisualizers.INT, width=2)
    sub_schema.add_field('x', label='X', type=GsiFieldVisualizers.FLOAT, width=2)
    sub_schema.add_field('z', label='Z', type=GsiFieldVisualizers.FLOAT, width=2)
    sub_schema.add_field('level', label='Level', type=GsiFieldVisualizers.STRING, width=2)
    sub_schema.add_field('cost', label='Cost', type=GsiFieldVisualizers.FLOAT, width=2)
    sub_schema.add_field('final_cost', label='Final Cost (lower==better)', type=GsiFieldVisualizers.FLOAT, width=2)
    sub_schema.add_field('result', label='Result', width=2)
    sub_schema.add_field('raw_result', label='Raw Result', type=GsiFieldVisualizers.INT, width=2)
    sub_schema.add_field('group', label='Group', type=GsiFieldVisualizers.INT, width=2)
    sub_schema.add_field('x', label='X', type=GsiFieldVisualizers.FLOAT, width=2)
    sub_schema.add_field('z', label='Z', type=GsiFieldVisualizers.FLOAT, width=2)
    sub_schema.add_field('level', label='Level', type=GsiFieldVisualizers.STRING, width=2)
    sub_schema.add_field('cost', label='Cost', type=GsiFieldVisualizers.FLOAT, width=2)
    sub_schema.add_field('result', label='Result', width=2)
    sub_schema.add_field('x', label='X', type=GsiFieldVisualizers.FLOAT, width=2)
    sub_schema.add_field('z', label='Z', type=GsiFieldVisualizers.FLOAT, width=2)
    sub_schema.add_field('level', label='Level', type=GsiFieldVisualizers.STRING, width=2)
    sub_schema.add_field('portal', label='Portal', type=GsiFieldVisualizers.STRING, width=2)
    sub_schema.add_field('qx', label='QX', type=GsiFieldVisualizers.FLOAT, width=2, hidden=True)
    sub_schema.add_field('qy', label='QY', type=GsiFieldVisualizers.FLOAT, width=2, hidden=True)
    sub_schema.add_field('qz', label='QZ', type=GsiFieldVisualizers.FLOAT, width=2, hidden=True)
    sub_schema.add_field('qw', label='QW', type=GsiFieldVisualizers.FLOAT, width=2, hidden=True)
    sub_schema.add_field('name', label='Name', type=GsiFieldVisualizers.STRING, width=2)
    sub_schema.add_field('value', label='Value', type=GsiFieldVisualizers.FLOAT, width=2)
    sub_schema.add_field('callstack', label='Callstack', width=2)
def surface_string(surface_id):
    out_str = str(surface_id.secondary_id) + '/'
    if surface_id.type == routing.SurfaceType.SURFACETYPE_WORLD:
        out_str = out_str + 'WORLD'
    elif surface_id.type == routing.SurfaceType.SURFACETYPE_OBJECT:
        out_str = out_str + 'OBJECT:' + str(surface_id.primary_id)
    elif surface_id.type == routing.SurfaceType.SURFACETYPE_POOL:
        out_str = out_str + 'POOL'
    else:
        out_str = out_str + 'UNKNOWN'
    return out_str

def archive_plan(planner, path, ticks, time):
    result = 'Success'
    if path.is_route_fail() or path.status == routing.Path.PLANSTATUS_FAILED:
        result = 'Failed'
    plan_time = 0.0
    plan_record = path.nodes.record
    if plan_record is not None:
        plan_time = plan_record['total_time_ms']
    entry = {'planner_name': str(planner), 'planner_id': str(hex(planner.id)), 'result': result, 'x': round(path.route.origin.position.x, 4), 'y': round(path.route.origin.position.y, 4), 'z': round(path.route.origin.position.z, 4), 'qx': round(path.route.origin.orientation.x, 4), 'qy': round(path.route.origin.orientation.y, 4), 'qz': round(path.route.origin.orientation.z, 4), 'qw': round(path.route.origin.orientation.w, 4), 'level': surface_string(path.route.origin.routing_surface), 'ticks': ticks, 'time': round(time*1000, 4), 'plan_time': round(plan_time, 4), 'dist': round(path.nodes.length, 4), 'num_goals': len(path.route.goals), 'num_starts': len(path.route.origins)}
    goal_mask_success = routing.GOAL_STATUS_SUCCESS | routing.GOAL_STATUS_SUCCESS_TRIVIAL | routing.GOAL_STATUS_SUCCESS_LOCAL
    goal_mask_input_error = routing.GOAL_STATUS_INVALID_SURFACE | routing.GOAL_STATUS_INVALID_POINT
    goal_mask_unreachable = routing.GOAL_STATUS_CONNECTIVITY_GROUP_UNREACHABLE | routing.GOAL_STATUS_COMPONENT_DIFFERENT | routing.GOAL_STATUS_IMPASSABLE | routing.GOAL_STATUS_BLOCKED
    goals = []
    index = 0
    for (goal, result) in zip(path.route.goals, path.nodes.goal_results()):
        result_str = 'UNKNOWN'
        if result[1] & goal_mask_success > 0:
            if result[1] & routing.GOAL_STATUS_LOWER_SCORE > 0:
                result_str = 'SUCCESS (Not Picked)'
            else:
                result_str = 'PICKED'
        if result[1] & goal_mask_unreachable > 0:
            result_str = 'UNREACHABLE'
        if result[1] & goal_mask_input_error > 0:
            result_str = 'INVALID'
        if result[1] & routing.GOAL_STATUS_NOTEVALUATED > 0:
            result_str = 'NOT EVALUATED'
        cost = round(result[2], 4)
        if cost >= 1000000.0:
            cost = 999999
        goals.append({'index': index, 'x': round(goal.location.position.x, 4), 'z': round(goal.location.position.z, 4), 'level': surface_string(goal.location.routing_surface), 'cost': round(goal.cost, 4), 'final_cost': cost, 'result': result_str, 'raw_result': result[1], 'group': goal.group})
        index += 1
    entry['Goals'] = goals
    selected_start_tag = path.nodes.selected_start_tag_tuple
    starts = []
    for start in path.route.origins:
        result = 'Not Chosen'
        starts.append({'x': round(start.location.position.x, 4), 'z': round(start.location.position.z, 4), 'level': surface_string(start.location.routing_surface), 'cost': round(start.cost, 4), 'result': result})
    entry['Starts'] = starts
    nodes = []
    cur_path = path
    while cur_path is not None:
        for node in cur_path.nodes:
            nodes.append({'x': node.position[0], 'z': node.position[2], 'level': surface_string(node.routing_surface_id), 'portal': str(node.portal_id) + '/' + str(node.portal_object_id), 'qx': node.orientation[0], 'qy': node.orientation[1], 'qz': node.orientation[2], 'qw': node.orientation[3]})
        cur_path = cur_path.next_path
    entry['Nodes'] = nodes
    details = []
    if plan_record is not None:
        for (name, value) in plan_record.items():
            details.append({'name': name, 'value': value})
    entry['Details'] = details
    callstack = []
    for line in traceback.format_stack():
        callstack.append({'callstack': line.strip()})
    callstack.reverse()
    entry['Callstack'] = callstack
    archiver.archive(data=entry, object_id=planner.id)

    sub_schema.add_field('name', label='Name', type=GsiFieldVisualizers.STRING, width=2)
    sub_schema.add_field('value', label='Value', type=GsiFieldVisualizers.FLOAT, width=2)
def archive_build(build_id):
    entry = {}
    build_record = routing.planner_build_record(build_id)
    if build_record is not None:
        entry = {'build_id': build_record['id'], 'total_time_ms': build_record['total_time_ms']}
    details = []
    if build_record is not None:
        for (name, value) in build_record.items():
            details.append({'name': name, 'value': value})
    entry['Details'] = details
    build_archiver.archive(data=entry)

    sub_schema.add_field('name', label='Name', type=GsiFieldVisualizers.STRING, width=2)
    sub_schema.add_field('value', label='Value', type=GsiFieldVisualizers.STRING, width=2)
    sub_schema.add_field('callstack', label='Callstack', width=2)
    sub_schema.add_field('loc', label='Loc', type=GsiFieldVisualizers.STRING, width=2)
def archive_FGL(fgl_id, context, result, time_s):
    obj = None
    if context.search_strategy.object_id != 0:
        obj = objects.system.find_object(context.search_strategy.object_id)
    if context.routing_context is not None:
        obj = objects.system.find_object(context.routing_context.agent_id)
    entry = {'fgl_id': fgl_id, 'object': str(obj), 'result': str(result), 'total_time_s': time_s}
    details = []
    for (name, value) in context.__dict__.items():
        details.append({'name': name, 'value': str(value)})
    entry['Details'] = details
    callstack = []
    for line in traceback.format_stack():
        callstack.append({'callstack': line.strip()})
    callstack.reverse()
    entry['Callstack'] = callstack
    results = []
    results_list = context.search.get_results()
    for loc in results_list:
        results.append({'loc': str(loc)})
    entry['Results'] = results
    FGL_archiver.archive(data=entry)
