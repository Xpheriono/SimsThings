from google.protobuf import descriptor
class SocialFriendMsg(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALFRIENDMSG

class SocialPersonaResponseMsg(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALPERSONARESPONSEMSG

class SocialId(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALID

class SocialGenericResponse(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALGENERICRESPONSE

class SocialPlayerInfoList(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class PlayerInfo(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _SOCIALPLAYERINFOLIST_PLAYERINFO

    DESCRIPTOR = _SOCIALPLAYERINFOLIST

class SocialFeedSubMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class SubscriptionFlags(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _SOCIALFEEDSUBMESSAGE_SUBSCRIPTIONFLAGS

    class SubscriptionObject(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _SOCIALFEEDSUBMESSAGE_SUBSCRIPTIONOBJECT

    DESCRIPTOR = _SOCIALFEEDSUBMESSAGE

class SocialSearchMsg(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALSEARCHMSG

class OriginErrorMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ORIGINERRORMESSAGE

class SocialInviteResponseMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALINVITERESPONSEMESSAGE

class SocialCassandraTest(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALCASSANDRATEST

class SocialFriendListRequestMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALFRIENDLISTREQUESTMESSAGE

class SocialRequestNucleusIdFromPersona(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALREQUESTNUCLEUSIDFROMPERSONA

class SocialNucleusIdFromPersonaResponse(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALNUCLEUSIDFROMPERSONARESPONSE

class SocialExchangeMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALEXCHANGEMESSAGE

class SocialFollowersMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALFOLLOWERSMESSAGE

class SocialFeedItemMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALFEEDITEMMESSAGE

class SocialFeedItemUnserializedMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALFEEDITEMUNSERIALIZEDMESSAGE

class SocialWallCommentMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALWALLCOMMENTMESSAGE

class SocialGetWallCommentsMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALGETWALLCOMMENTSMESSAGE

class SocialPostWallCommentMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALPOSTWALLCOMMENTMESSAGE

class SocialDeleteWallCommentMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALDELETEWALLCOMMENTMESSAGE

class SocialRequestFeedWallMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALREQUESTFEEDWALLMESSAGE

class SocialRequestFollowersMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALREQUESTFOLLOWERSMESSAGE

class SocialResponseFollowersMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class PlayerFollower(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _SOCIALRESPONSEFOLLOWERSMESSAGE_PLAYERFOLLOWER

    DESCRIPTOR = _SOCIALRESPONSEFOLLOWERSMESSAGE

class SocialCommentPetitionMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALCOMMENTPETITIONMESSAGE

class SocialBioPetitionMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALBIOPETITIONMESSAGE

class SocialFeedRemovalMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALFEEDREMOVALMESSAGE

class SocialControlMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALCONTROLMESSAGE

class SocialInvalidateMsg(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALINVALIDATEMSG

class SocialControlQueueBroadcastMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALCONTROLQUEUEBROADCASTMESSAGE

class LifeEventMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _LIFEEVENTMESSAGE

class SocialFacebookEventMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALFACEBOOKEVENTMESSAGE
