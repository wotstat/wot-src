package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.epicBattle.VO.daapi.EpicPlayerStatsVO;
   import net.wg.gui.battle.epicBattle.VO.daapi.EpicVehiclesStatsVO;
   import net.wg.infrastructure.exceptions.AbstractException;
   import net.wg.infrastructure.helpers.statisticsDataController.BattleStatisticDataController;
   
   public class EpicBattleStatisticDataControllerMeta extends BattleStatisticDataController
   {
      
      private var _epicPlayerStatsVO:EpicPlayerStatsVO;
      
      private var _epicVehiclesStatsVO:EpicVehiclesStatsVO;
      
      public function EpicBattleStatisticDataControllerMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(Boolean(this._epicPlayerStatsVO))
         {
            this._epicPlayerStatsVO.dispose();
            this._epicPlayerStatsVO = null;
         }
         if(Boolean(this._epicVehiclesStatsVO))
         {
            this._epicVehiclesStatsVO.dispose();
            this._epicVehiclesStatsVO = null;
         }
         super.onDispose();
      }
      
      final public function as_updateEpicPlayerStats(param1:Object) : void
      {
         var _loc2_:EpicPlayerStatsVO = this._epicPlayerStatsVO;
         this._epicPlayerStatsVO = new EpicPlayerStatsVO(param1);
         this.updateEpicPlayerStats(this._epicPlayerStatsVO);
         if(Boolean(_loc2_))
         {
            _loc2_.dispose();
         }
      }
      
      final public function as_setEpicVehiclesStats(param1:Object) : void
      {
         var _loc2_:EpicVehiclesStatsVO = this._epicVehiclesStatsVO;
         this._epicVehiclesStatsVO = new EpicVehiclesStatsVO(param1);
         this.setEpicVehiclesStats(this._epicVehiclesStatsVO);
         if(Boolean(_loc2_))
         {
            _loc2_.dispose();
         }
      }
      
      final public function as_updateEpicVehiclesStats(param1:Object) : void
      {
         var _loc2_:EpicVehiclesStatsVO = new EpicVehiclesStatsVO(param1);
         this.updateEpicVehiclesStats(_loc2_);
      }
      
      protected function updateEpicPlayerStats(param1:EpicPlayerStatsVO) : void
      {
         var _loc2_:String = "as_updateEpicPlayerStats" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function setEpicVehiclesStats(param1:EpicVehiclesStatsVO) : void
      {
         var _loc2_:String = "as_setEpicVehiclesStats" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function updateEpicVehiclesStats(param1:EpicVehiclesStatsVO) : void
      {
         var _loc2_:String = "as_updateEpicVehiclesStats" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}

