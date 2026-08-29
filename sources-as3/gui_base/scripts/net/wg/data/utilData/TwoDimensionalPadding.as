package net.wg.data.utilData
{
   import flash.geom.Point;
   
   public class TwoDimensionalPadding
   {
      
      public var top:Point = new Point();
      
      public var bottom:Point = new Point();
      
      public var left:Point = new Point();
      
      public var right:Point = new Point();
      
      public function TwoDimensionalPadding(param1:Point = null, param2:Point = null, param3:Point = null, param4:Point = null)
      {
         super();
         if(Boolean(param1))
         {
            this.top = param1;
         }
         if(Boolean(param2))
         {
            this.right = param2;
         }
         if(Boolean(param3))
         {
            this.bottom = param3;
         }
         if(Boolean(param4))
         {
            this.left = param4;
         }
      }
   }
}

