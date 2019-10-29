from google.protobuf import descriptorfrom google.protobuf import messagefrom google.protobuf import reflectionfrom google.protobuf import descriptor_pb2import protocolbuffers.Consts_pb2 as Consts_pb2import protocolbuffers.Math_pb2 as Math_pb2import protocolbuffers.ResourceKey_pb2 as ResourceKey_pb2DESCRIPTOR = descriptor.FileDescriptor(name='Animation.proto', package='EA.Sims4.Network', serialized_pb='\n\x0fAnimation.proto\x12\x10EA.Sims4.Network\x1a\x0cConsts.proto\x1a\nMath.proto\x1a\x11ResourceKey.proto"J\n\x15AnimationEventHandler\x12\x12\n\nevent_type\x18\x01 \x02(\r\x12\x10\n\x08event_id\x18\x02 \x02(\r\x12\x0b\n\x03tag\x18\x03 \x02(\x04"�\x01\n\x15AnimationRequestBlock\x12\x10\n\x08arb_data\x18\x01 \x02(\x0c\x12?\n\x0eevent_handlers\x18\x02 \x03(\x0b2\'.EA.Sims4.Network.AnimationEventHandler\x12;\n\x10objects_to_reset\x18\x03 \x03(\x0b2!.EA.Sims4.Network.ManagerObjectId\x12\x1f\n\x10is_interruptible\x18\x04 \x01(\x08:\x05false\x12\x1d\n\x0eshould_analyze\x18\x05 \x01(\x08:\x05false"k\n\x15AnimationStateRequest\x12*\n\x03asm\x18\x01 \x01(\x0b2\x1d.EA.Sims4.Network.ResourceKey\x12\x12\n\nstate_name\x18\x02 \x01(\t\x12\x12\n\nactor_name\x18\x03 \x01(\t"6\n\tCurveData\x12\x13\n\x0binput_value\x18\x01 \x02(\x02\x12\x14\n\x0coutput_value\x18\x02 \x02(\x02"�\x03\n\nFocusEvent\x124\n\x04type\x18\x01 \x02(\x0e2&.EA.Sims4.Network.FocusEvent.EventType\x12\n\n\x02id\x18\x02 \x01(\r\x12\r\n\x05layer\x18\x03 \x01(\r\x12\r\n\x05flags\x18\x04 \x01(\r\x12\r\n\x05score\x18\x05 \x01(\x02\x12\x17\n\x0fjoint_name_hash\x18\x06 \x01(\r\x12\x11\n\ttarget_id\x18\x07 \x01(\x04\x12)\n\x06offset\x18\x08 \x01(\x0b2\x19.EA.Sims4.Network.Vector3\x123\n\x0edistance_curve\x18\t \x03(\x0b2\x1b.EA.Sims4.Network.CurveData\x121\n\x0cfacing_curve\x18\n \x03(\x0b2\x1b.EA.Sims4.Network.CurveData\x12\x11\n\tsource_id\x18\x0b \x01(\x04"\x91\x01\n\tEventType\x12\r\n\tFOCUS_ADD\x10\x00\x12\x10\n\x0cFOCUS_DELETE\x10\x01\x12\x0f\n\x0bFOCUS_CLEAR\x10\x02\x12\x16\n\x12FOCUS_MODIFY_SCORE\x10\x03\x12\x11\n\rFOCUS_DISABLE\x10\x04\x12\x16\n\x12FOCUS_FORCE_UPDATE\x10\x05\x12\x0f\n\x0bFOCUS_PRINT\x10\x06"\x96\x06\n\x17ConfigureAwarenessActor\x12F\n\x12channels_to_remove\x18\x03 \x03(\x0e2&.EA.Sims4.Network.AwarenessChannelNameB\x02\x10\x01\x12W\n\x15channels_to_configure\x18\x04 \x03(\x0b28.EA.Sims4.Network.ConfigureAwarenessActor.ChannelOptions\x12\x1e\n\x16proximity_inner_radius\x18\x05 \x01(\x02\x12\x1e\n\x16proximity_outer_radius\x18\x06 \x01(\x02\x1a�\x02\n\x0eChannelOptions\x124\n\x04name\x18\x01 \x02(\x0e2&.EA.Sims4.Network.AwarenessChannelName\x12R\n\teval_mode\x18\x02 \x01(\x0e2?.EA.Sims4.Network.ConfigureAwarenessActor.ChannelEvaluationMode\x12\x0c\n\x04gate\x18\x03 \x01(\x02\x12\x0c\n\x04gain\x18\x04 \x01(\x02\x12\r\n\x05limit\x18\x05 \x01(\x02\x12\x1f\n\x17trigger_threshold_delta\x18\x06 \x01(\x02\x12\x11\n\ttype_name\x18\x07 \x01(\t\x12\x16\n\thold_time\x18\x08 \x01(\x02:\x031.5\x12\x1b\n\x0ecool_down_time\x18\t \x01(\x02:\x031.5"�\x01\n\x15ChannelEvaluationMode\x12#\n\x1fAWARENESS_CHANNEL_EVALMODE_PEAK\x10\x00\x12&\n"AWARENESS_CHANNEL_EVALMODE_AVERAGE\x10\x01\x12"\n\x1eAWARENESS_CHANNEL_EVALMODE_SUM\x10\x02\x12,\n(AWARENESS_CHANNEL_EVALMODE_SUM_SPLITSIGN\x10\x03\x120\n,AWARENESS_CHANNEL_EVALMODE_AVERAGE_SPLITSIGN\x10\x04"�\x02\n\x1eConfigureAwarenessSourceObject\x12f\n\x17gameplay_channel_values\x18\x03 \x03(\x0b2E.EA.Sims4.Network.ConfigureAwarenessSourceObject.GameplayChannelValue\x12\x1f\n\x17audio_volume_multiplier\x18\x04 \x01(\x02\x12 \n\x18audio_full_volume_radius\x18\x05 \x01(\x02\x12\x1c\n\x14audio_falloff_radius\x18\x06 \x01(\x02\x1a[\n\x14GameplayChannelValue\x124\n\x04name\x18\x01 \x02(\x0e2&.EA.Sims4.Network.AwarenessChannelName\x12\r\n\x05value\x18\x02 \x02(\x02*�\x03\n\x14AwarenessChannelName\x12\x1f\n\x1bAWARENESS_CHANNEL_PROXIMITY\x10\x00\x12"\n\x1eAWARENESS_CHANNEL_AUDIO_VOLUME\x10\x01\x12!\n\x1cAWARENESS_CHANNEL_GAMEPLAY_0\x10�\x07\x12!\n\x1cAWARENESS_CHANNEL_GAMEPLAY_1\x10�\x07\x12!\n\x1cAWARENESS_CHANNEL_GAMEPLAY_2\x10�\x07\x12!\n\x1cAWARENESS_CHANNEL_GAMEPLAY_3\x10�\x07\x12!\n\x1cAWARENESS_CHANNEL_GAMEPLAY_4\x10�\x07\x12!\n\x1cAWARENESS_CHANNEL_GAMEPLAY_5\x10�\x07\x12!\n\x1cAWARENESS_CHANNEL_GAMEPLAY_6\x10�\x07\x12!\n\x1cAWARENESS_CHANNEL_GAMEPLAY_7\x10�\x07\x12!\n\x1cAWARENESS_CHANNEL_GAMEPLAY_8\x10�\x07\x12!\n\x1cAWARENESS_CHANNEL_GAMEPLAY_9\x10�\x07')_AWARENESSCHANNELNAME = descriptor.EnumDescriptor(name='AwarenessChannelName', full_name='EA.Sims4.Network.AwarenessChannelName', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_PROXIMITY', index=0, number=0, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_AUDIO_VOLUME', index=1, number=1, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_GAMEPLAY_0', index=2, number=1000, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_GAMEPLAY_1', index=3, number=1001, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_GAMEPLAY_2', index=4, number=1002, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_GAMEPLAY_3', index=5, number=1003, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_GAMEPLAY_4', index=6, number=1004, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_GAMEPLAY_5', index=7, number=1005, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_GAMEPLAY_6', index=8, number=1006, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_GAMEPLAY_7', index=9, number=1007, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_GAMEPLAY_8', index=10, number=1008, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_GAMEPLAY_9', index=11, number=1009, options=None, type=None)], containing_type=None, options=None, serialized_start=2164, serialized_end=2605)AWARENESS_CHANNEL_PROXIMITY = 0AWARENESS_CHANNEL_AUDIO_VOLUME = 1AWARENESS_CHANNEL_GAMEPLAY_0 = 1000AWARENESS_CHANNEL_GAMEPLAY_1 = 1001AWARENESS_CHANNEL_GAMEPLAY_2 = 1002AWARENESS_CHANNEL_GAMEPLAY_3 = 1003AWARENESS_CHANNEL_GAMEPLAY_4 = 1004AWARENESS_CHANNEL_GAMEPLAY_5 = 1005AWARENESS_CHANNEL_GAMEPLAY_6 = 1006AWARENESS_CHANNEL_GAMEPLAY_7 = 1007AWARENESS_CHANNEL_GAMEPLAY_8 = 1008AWARENESS_CHANNEL_GAMEPLAY_9 = 1009_FOCUSEVENT_EVENTTYPE = descriptor.EnumDescriptor(name='EventType', full_name='EA.Sims4.Network.FocusEvent.EventType', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='FOCUS_ADD', index=0, number=0, options=None, type=None), descriptor.EnumValueDescriptor(name='FOCUS_DELETE', index=1, number=1, options=None, type=None), descriptor.EnumValueDescriptor(name='FOCUS_CLEAR', index=2, number=2, options=None, type=None), descriptor.EnumValueDescriptor(name='FOCUS_MODIFY_SCORE', index=3, number=3, options=None, type=None), descriptor.EnumValueDescriptor(name='FOCUS_DISABLE', index=4, number=4, options=None, type=None), descriptor.EnumValueDescriptor(name='FOCUS_FORCE_UPDATE', index=5, number=5, options=None, type=None), descriptor.EnumValueDescriptor(name='FOCUS_PRINT', index=6, number=6, options=None, type=None)], containing_type=None, options=None, serialized_start=894, serialized_end=1039)_CONFIGUREAWARENESSACTOR_CHANNELEVALUATIONMODE = descriptor.EnumDescriptor(name='ChannelEvaluationMode', full_name='EA.Sims4.Network.ConfigureAwarenessActor.ChannelEvaluationMode', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_EVALMODE_PEAK', index=0, number=0, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_EVALMODE_AVERAGE', index=1, number=1, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_EVALMODE_SUM', index=2, number=2, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_EVALMODE_SUM_SPLITSIGN', index=3, number=3, options=None, type=None), descriptor.EnumValueDescriptor(name='AWARENESS_CHANNEL_EVALMODE_AVERAGE_SPLITSIGN', index=4, number=4, options=None, type=None)], containing_type=None, options=None, serialized_start=1600, serialized_end=1832)_ANIMATIONEVENTHANDLER = descriptor.Descriptor(name='AnimationEventHandler', full_name='EA.Sims4.Network.AnimationEventHandler', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='event_type', full_name='EA.Sims4.Network.AnimationEventHandler.event_type', index=0, number=1, type=13, cpp_type=3, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='event_id', full_name='EA.Sims4.Network.AnimationEventHandler.event_id', index=1, number=2, type=13, cpp_type=3, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='tag', full_name='EA.Sims4.Network.AnimationEventHandler.tag', index=2, number=3, type=4, cpp_type=4, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=82, serialized_end=156)_ANIMATIONREQUESTBLOCK = descriptor.Descriptor(name='AnimationRequestBlock', full_name='EA.Sims4.Network.AnimationRequestBlock', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='arb_data', full_name='EA.Sims4.Network.AnimationRequestBlock.arb_data', index=0, number=1, type=12, cpp_type=9, label=2, has_default_value=False, default_value=b'', message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='event_handlers', full_name='EA.Sims4.Network.AnimationRequestBlock.event_handlers', index=1, number=2, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='objects_to_reset', full_name='EA.Sims4.Network.AnimationRequestBlock.objects_to_reset', index=2, number=3, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='is_interruptible', full_name='EA.Sims4.Network.AnimationRequestBlock.is_interruptible', index=3, number=4, type=8, cpp_type=7, label=1, has_default_value=True, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='should_analyze', full_name='EA.Sims4.Network.AnimationRequestBlock.should_analyze', index=4, number=5, type=8, cpp_type=7, label=1, has_default_value=True, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=159, serialized_end=390)_ANIMATIONSTATEREQUEST = descriptor.Descriptor(name='AnimationStateRequest', full_name='EA.Sims4.Network.AnimationStateRequest', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='asm', full_name='EA.Sims4.Network.AnimationStateRequest.asm', index=0, number=1, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='state_name', full_name='EA.Sims4.Network.AnimationStateRequest.state_name', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='actor_name', full_name='EA.Sims4.Network.AnimationStateRequest.actor_name', index=2, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=392, serialized_end=499)_CURVEDATA = descriptor.Descriptor(name='CurveData', full_name='EA.Sims4.Network.CurveData', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='input_value', full_name='EA.Sims4.Network.CurveData.input_value', index=0, number=1, type=2, cpp_type=6, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='output_value', full_name='EA.Sims4.Network.CurveData.output_value', index=1, number=2, type=2, cpp_type=6, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=501, serialized_end=555)_FOCUSEVENT = descriptor.Descriptor(name='FocusEvent', full_name='EA.Sims4.Network.FocusEvent', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='type', full_name='EA.Sims4.Network.FocusEvent.type', index=0, number=1, type=14, cpp_type=8, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='id', full_name='EA.Sims4.Network.FocusEvent.id', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='layer', full_name='EA.Sims4.Network.FocusEvent.layer', index=2, number=3, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='flags', full_name='EA.Sims4.Network.FocusEvent.flags', index=3, number=4, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='score', full_name='EA.Sims4.Network.FocusEvent.score', index=4, number=5, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='joint_name_hash', full_name='EA.Sims4.Network.FocusEvent.joint_name_hash', index=5, number=6, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='target_id', full_name='EA.Sims4.Network.FocusEvent.target_id', index=6, number=7, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='offset', full_name='EA.Sims4.Network.FocusEvent.offset', index=7, number=8, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='distance_curve', full_name='EA.Sims4.Network.FocusEvent.distance_curve', index=8, number=9, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='facing_curve', full_name='EA.Sims4.Network.FocusEvent.facing_curve', index=9, number=10, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='source_id', full_name='EA.Sims4.Network.FocusEvent.source_id', index=10, number=11, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[_FOCUSEVENT_EVENTTYPE], options=None, is_extendable=False, extension_ranges=[], serialized_start=558, serialized_end=1039)_CONFIGUREAWARENESSACTOR_CHANNELOPTIONS = descriptor.Descriptor(name='ChannelOptions', full_name='EA.Sims4.Network.ConfigureAwarenessActor.ChannelOptions', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='name', full_name='EA.Sims4.Network.ConfigureAwarenessActor.ChannelOptions.name', index=0, number=1, type=14, cpp_type=8, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='eval_mode', full_name='EA.Sims4.Network.ConfigureAwarenessActor.ChannelOptions.eval_mode', index=1, number=2, type=14, cpp_type=8, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='gate', full_name='EA.Sims4.Network.ConfigureAwarenessActor.ChannelOptions.gate', index=2, number=3, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='gain', full_name='EA.Sims4.Network.ConfigureAwarenessActor.ChannelOptions.gain', index=3, number=4, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='limit', full_name='EA.Sims4.Network.ConfigureAwarenessActor.ChannelOptions.limit', index=4, number=5, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='trigger_threshold_delta', full_name='EA.Sims4.Network.ConfigureAwarenessActor.ChannelOptions.trigger_threshold_delta', index=5, number=6, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='type_name', full_name='EA.Sims4.Network.ConfigureAwarenessActor.ChannelOptions.type_name', index=6, number=7, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='hold_time', full_name='EA.Sims4.Network.ConfigureAwarenessActor.ChannelOptions.hold_time', index=7, number=8, type=2, cpp_type=6, label=1, has_default_value=True, default_value=1.5, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='cool_down_time', full_name='EA.Sims4.Network.ConfigureAwarenessActor.ChannelOptions.cool_down_time', index=8, number=9, type=2, cpp_type=6, label=1, has_default_value=True, default_value=1.5, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1295, serialized_end=1597)_CONFIGUREAWARENESSACTOR = descriptor.Descriptor(name='ConfigureAwarenessActor', full_name='EA.Sims4.Network.ConfigureAwarenessActor', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='channels_to_remove', full_name='EA.Sims4.Network.ConfigureAwarenessActor.channels_to_remove', index=0, number=3, type=14, cpp_type=8, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\x10\x01')), descriptor.FieldDescriptor(name='channels_to_configure', full_name='EA.Sims4.Network.ConfigureAwarenessActor.channels_to_configure', index=1, number=4, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='proximity_inner_radius', full_name='EA.Sims4.Network.ConfigureAwarenessActor.proximity_inner_radius', index=2, number=5, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='proximity_outer_radius', full_name='EA.Sims4.Network.ConfigureAwarenessActor.proximity_outer_radius', index=3, number=6, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[_CONFIGUREAWARENESSACTOR_CHANNELOPTIONS], enum_types=[_CONFIGUREAWARENESSACTOR_CHANNELEVALUATIONMODE], options=None, is_extendable=False, extension_ranges=[], serialized_start=1042, serialized_end=1832)_CONFIGUREAWARENESSSOURCEOBJECT_GAMEPLAYCHANNELVALUE = descriptor.Descriptor(name='GameplayChannelValue', full_name='EA.Sims4.Network.ConfigureAwarenessSourceObject.GameplayChannelValue', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='name', full_name='EA.Sims4.Network.ConfigureAwarenessSourceObject.GameplayChannelValue.name', index=0, number=1, type=14, cpp_type=8, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='value', full_name='EA.Sims4.Network.ConfigureAwarenessSourceObject.GameplayChannelValue.value', index=1, number=2, type=2, cpp_type=6, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=2070, serialized_end=2161)_CONFIGUREAWARENESSSOURCEOBJECT = descriptor.Descriptor(name='ConfigureAwarenessSourceObject', full_name='EA.Sims4.Network.ConfigureAwarenessSourceObject', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='gameplay_channel_values', full_name='EA.Sims4.Network.ConfigureAwarenessSourceObject.gameplay_channel_values', index=0, number=3, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='audio_volume_multiplier', full_name='EA.Sims4.Network.ConfigureAwarenessSourceObject.audio_volume_multiplier', index=1, number=4, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='audio_full_volume_radius', full_name='EA.Sims4.Network.ConfigureAwarenessSourceObject.audio_full_volume_radius', index=2, number=5, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='audio_falloff_radius', full_name='EA.Sims4.Network.ConfigureAwarenessSourceObject.audio_falloff_radius', index=3, number=6, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[_CONFIGUREAWARENESSSOURCEOBJECT_GAMEPLAYCHANNELVALUE], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1835, serialized_end=2161)_ANIMATIONREQUESTBLOCK.fields_by_name['event_handlers'].message_type = _ANIMATIONEVENTHANDLER_ANIMATIONREQUESTBLOCK.fields_by_name['objects_to_reset'].message_type = Consts_pb2._MANAGEROBJECTID_ANIMATIONSTATEREQUEST.fields_by_name['asm'].message_type = ResourceKey_pb2._RESOURCEKEY_FOCUSEVENT.fields_by_name['type'].enum_type = _FOCUSEVENT_EVENTTYPE_FOCUSEVENT.fields_by_name['offset'].message_type = Math_pb2._VECTOR3_FOCUSEVENT.fields_by_name['distance_curve'].message_type = _CURVEDATA_FOCUSEVENT.fields_by_name['facing_curve'].message_type = _CURVEDATA_FOCUSEVENT_EVENTTYPE.containing_type = _FOCUSEVENT_CONFIGUREAWARENESSACTOR_CHANNELOPTIONS.fields_by_name['name'].enum_type = _AWARENESSCHANNELNAME_CONFIGUREAWARENESSACTOR_CHANNELOPTIONS.fields_by_name['eval_mode'].enum_type = _CONFIGUREAWARENESSACTOR_CHANNELEVALUATIONMODE_CONFIGUREAWARENESSACTOR_CHANNELOPTIONS.containing_type = _CONFIGUREAWARENESSACTOR_CONFIGUREAWARENESSACTOR.fields_by_name['channels_to_remove'].enum_type = _AWARENESSCHANNELNAME_CONFIGUREAWARENESSACTOR.fields_by_name['channels_to_configure'].message_type = _CONFIGUREAWARENESSACTOR_CHANNELOPTIONS_CONFIGUREAWARENESSACTOR_CHANNELEVALUATIONMODE.containing_type = _CONFIGUREAWARENESSACTOR_CONFIGUREAWARENESSSOURCEOBJECT_GAMEPLAYCHANNELVALUE.fields_by_name['name'].enum_type = _AWARENESSCHANNELNAME_CONFIGUREAWARENESSSOURCEOBJECT_GAMEPLAYCHANNELVALUE.containing_type = _CONFIGUREAWARENESSSOURCEOBJECT_CONFIGUREAWARENESSSOURCEOBJECT.fields_by_name['gameplay_channel_values'].message_type = _CONFIGUREAWARENESSSOURCEOBJECT_GAMEPLAYCHANNELVALUEDESCRIPTOR.message_types_by_name['AnimationEventHandler'] = _ANIMATIONEVENTHANDLERDESCRIPTOR.message_types_by_name['AnimationRequestBlock'] = _ANIMATIONREQUESTBLOCKDESCRIPTOR.message_types_by_name['AnimationStateRequest'] = _ANIMATIONSTATEREQUESTDESCRIPTOR.message_types_by_name['CurveData'] = _CURVEDATADESCRIPTOR.message_types_by_name['FocusEvent'] = _FOCUSEVENTDESCRIPTOR.message_types_by_name['ConfigureAwarenessActor'] = _CONFIGUREAWARENESSACTORDESCRIPTOR.message_types_by_name['ConfigureAwarenessSourceObject'] = _CONFIGUREAWARENESSSOURCEOBJECT
class AnimationEventHandler(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ANIMATIONEVENTHANDLER

class AnimationRequestBlock(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ANIMATIONREQUESTBLOCK

class AnimationStateRequest(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ANIMATIONSTATEREQUEST

class CurveData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _CURVEDATA

class FocusEvent(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _FOCUSEVENT

class ConfigureAwarenessActor(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class ChannelOptions(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _CONFIGUREAWARENESSACTOR_CHANNELOPTIONS

    DESCRIPTOR = _CONFIGUREAWARENESSACTOR

class ConfigureAwarenessSourceObject(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class GameplayChannelValue(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _CONFIGUREAWARENESSSOURCEOBJECT_GAMEPLAYCHANNELVALUE

    DESCRIPTOR = _CONFIGUREAWARENESSSOURCEOBJECT
