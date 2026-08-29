from gui.battle_results.components import base, maps_training
_MAPS_TRAINING_VO_META = base.DictMeta({b'result': {}, b'goal': {}, b'duration': 0, 
   b'stats': [], b'geometryId': 0, 
   b'team': 0, 
   b'vehicle': {}, b'doneValue': (-1), 
   b'wasDone': False, 
   b'scenarioProgress': [], b'rewards': [], b'accountProgress': {}})
_MAPS_TRAINING_RESULT_VO_META = base.DictMeta({b'str': b'', 
   b'value': b'', 
   b'win': False})
_MAPS_TRAINING_BATTLE_GOAL_VO_META = base.DictMeta({b'heavyTank': [
                0, 0], 
   b'mediumTank': [
                 0, 0], 
   b'lightTank': [
                0, 0], 
   b'SPG': [
          0, 0], 
   b'AT-SPG': [
             0, 0]})
_MAPS_TRAINING_VEHICLE_VO_META = base.DictMeta({b'type': b'', 
   b'name': b''})
_MAPS_TRAINING_ACC_PROGRESS_VO_META = base.DictMeta({b'hasImproved': False})
_components = (
 maps_training.BattleResultBlock(_MAPS_TRAINING_RESULT_VO_META, b'result'),
 maps_training.BattleGoalsBlock(_MAPS_TRAINING_BATTLE_GOAL_VO_META, b'goal'),
 maps_training.BattleDurationItem(b'duration'),
 maps_training.StatsBlock(base.ListMeta(), b'stats'),
 maps_training.GeometryIdItem(b'geometryId'),
 maps_training.TeamItem(b'team'),
 maps_training.VehicleBlock(_MAPS_TRAINING_VEHICLE_VO_META, b'vehicle'),
 maps_training.DoneValueItem(b'doneValue'),
 maps_training.WasDoneItem(b'wasDone'),
 maps_training.ScenarioProgressBlock(base.ListMeta(), b'scenarioProgress'),
 maps_training.RewardsBlock(base.ListMeta(), b'rewards'),
 maps_training.AccountProgressBlock(_MAPS_TRAINING_ACC_PROGRESS_VO_META, b'accountProgress'))
MAPS_TRAINING_RESULTS_BLOCK = base.StatsBlock(_MAPS_TRAINING_VO_META, b'')
for i, component in enumerate(_components):
    MAPS_TRAINING_RESULTS_BLOCK.addComponent(i, component)
