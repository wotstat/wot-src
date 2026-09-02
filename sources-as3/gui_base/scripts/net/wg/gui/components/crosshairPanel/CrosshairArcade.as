package net.wg.gui.components.crosshairPanel
{
   import net.wg.gui.components.crosshairPanel.wt.WTCrosshairBase;
   
   public class CrosshairArcade extends WTCrosshairBase
   {
      
      private static const GUN_COOLING_INDICATOR_OFFSET:int = -100;
      
      private var _reloadTimeBlinkYPositions:Array = [9,39,10,39,22];
      
      private var _abilityModifierXPositions:Array = [160,211,160,155,155];
      
      public function CrosshairArcade()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this._reloadTimeBlinkYPositions.splice(0,this._reloadTimeBlinkYPositions.length);
         this._reloadTimeBlinkYPositions = null;
         this._abilityModifierXPositions.splice(0,this._abilityModifierXPositions.length);
         this._abilityModifierXPositions = null;
         super.onDispose();
      }
      
      override protected function getReloadTimeBlinkYPos() : Array
      {
         return this._reloadTimeBlinkYPositions;
      }
      
      override protected function getAbilityModifierXPos() : Array
      {
         return this._abilityModifierXPositions;
      }
      
      override protected function getGunCoolingIndicatorYOffset() : int
      {
         return GUN_COOLING_INDICATOR_OFFSET;
      }
   }
}

