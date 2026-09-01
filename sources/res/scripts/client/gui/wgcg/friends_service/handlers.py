from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class FriendServiceRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.FRIEND_STATE): (self.__getFriendBalance), 
           (WebRequestDataType.FRIEND_LIST): (self.__getFriendList), 
           (WebRequestDataType.PUT_BEST_FRIEND): (self.__putBestFriend), 
           (WebRequestDataType.DELETE_BEST_FRIEND): (self.__deleteBestFriend), 
           (WebRequestDataType.POST_GATHER_FRIEND_NY_RESOURCES): (self.__gatherFriendResources)}
        return handlers

    def __getFriendBalance(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'friends', b'get_friend_balance'), ctx.getSpaId())

    def __getFriendList(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'friends', b'get_friend_list'))

    def __putBestFriend(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'friends', b'put_best_friend'), ctx.getSpaId())

    def __deleteBestFriend(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'friends', b'delete_best_friend'), ctx.getSpaId())

    def __gatherFriendResources(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'friends', b'post_gather_friend_ny_resources'), ctx.getSpaId())
