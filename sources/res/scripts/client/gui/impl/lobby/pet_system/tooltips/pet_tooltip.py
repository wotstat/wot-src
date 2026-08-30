from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.pet_system.tooltips.pet_tooltip_model import PetTooltipModel
from gui.impl.pub import ViewImpl

class PetTooltip(ViewImpl):

    def __init__(self, context=None, *args, **kwargs):
        settings = ViewSettings(R.views.mono.pet_system.tooltips.pet_tooltip())
        settings.model = PetTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        self.context = context
        super(PetTooltip, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(PetTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(PetTooltip, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as model:
            model.setPetNameID(self.context[b'petNameID'])
            model.setPetType(self.context[b'petType'])
            model.setBreedName(self.context[b'breedName'])
            model.setPetID(self.context[b'petID'])
            model.setPromotionBonuses(self.context[b'promotionBonuses'])
        return
