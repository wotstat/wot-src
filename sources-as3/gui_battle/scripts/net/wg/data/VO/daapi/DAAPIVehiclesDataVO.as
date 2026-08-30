package net.wg.data.VO.daapi
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class DAAPIVehiclesDataVO extends DAAPIDataClass
   {
      
      protected static const COND_LEFT_INFO_FIELD_NAME:String = "leftItems";
      
      protected static const COND_RIGHT_INFO_FIELD_NAME:String = "rightItems";
      
      protected static const COND_LEFT_VIDS_FIELD_NAME:String = "leftItemsIDs";
      
      protected static const COND_RIGHT_VIDS_FIELD_NAME:String = "rightItemsIDs";
      
      protected static const COND_LEFT_CIDS_FIELD_NAME:String = "leftCorrelationIDs";
      
      protected static const COND_RIGHT_CIDS_FIELD_NAME:String = "rightCorrelationIDs";
      
      public var leftVehicleInfos:Vector.<DAAPIVehicleInfoVO> = null;
      
      public var rightVehicleInfos:Vector.<DAAPIVehicleInfoVO> = null;
      
      public var leftVehiclesIDs:Vector.<Number> = null;
      
      public var rightVehiclesIDs:Vector.<Number> = null;
      
      public var leftCorrelationIDs:Vector.<Number> = null;
      
      public var rightCorrelationIDs:Vector.<Number> = null;
      
      public function DAAPIVehiclesDataVO(param1:Object)
      {
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         switch(param1)
         {
            case COND_LEFT_INFO_FIELD_NAME:
               this.leftVehicleInfos = Vector.<DAAPIVehicleInfoVO>(App.utils.data.convertVOArrayToVector(param1,param2,DAAPIVehicleInfoVO));
               return false;
            case COND_RIGHT_INFO_FIELD_NAME:
               this.rightVehicleInfos = Vector.<DAAPIVehicleInfoVO>(App.utils.data.convertVOArrayToVector(param1,param2,DAAPIVehicleInfoVO));
               return false;
            case COND_LEFT_VIDS_FIELD_NAME:
               if(Boolean(param2))
               {
                  this.leftVehiclesIDs = App.utils.data.convertNumberArrayToVector(param1,param2);
               }
               return false;
            case COND_RIGHT_VIDS_FIELD_NAME:
               if(Boolean(param2))
               {
                  this.rightVehiclesIDs = App.utils.data.convertNumberArrayToVector(param1,param2);
               }
               return false;
            case COND_LEFT_CIDS_FIELD_NAME:
               if(Boolean(param2))
               {
                  this.leftCorrelationIDs = App.utils.data.convertNumberArrayToVector(param1,param2);
               }
               return false;
            case COND_RIGHT_CIDS_FIELD_NAME:
               if(Boolean(param2))
               {
                  this.rightCorrelationIDs = App.utils.data.convertNumberArrayToVector(param1,param2);
               }
               return false;
            default:
               return super.onDataWrite(param1,param2);
         }
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:DAAPIVehicleInfoVO = null;
         if(Boolean(this.leftVehicleInfos))
         {
            for each(_loc1_ in this.leftVehicleInfos)
            {
               _loc1_.dispose();
            }
            this.leftVehicleInfos.fixed = false;
            this.leftVehicleInfos.splice(0,this.leftVehicleInfos.length);
            this.leftVehicleInfos = null;
         }
         if(Boolean(this.rightVehicleInfos))
         {
            for each(_loc1_ in this.rightVehicleInfos)
            {
               _loc1_.dispose();
            }
            this.rightVehicleInfos.fixed = false;
            this.rightVehicleInfos.splice(0,this.rightVehicleInfos.length);
            this.rightVehicleInfos = null;
         }
         if(Boolean(this.leftVehiclesIDs))
         {
            this.leftVehiclesIDs = null;
         }
         if(Boolean(this.rightVehiclesIDs))
         {
            this.rightVehiclesIDs = null;
         }
         if(Boolean(this.leftCorrelationIDs))
         {
            this.leftCorrelationIDs = null;
         }
         if(Boolean(this.rightCorrelationIDs))
         {
            this.rightCorrelationIDs = null;
         }
         super.onDispose();
      }
   }
}

