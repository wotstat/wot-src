import re
from abc import ABCMeta, abstractmethod
import typing
from Event import Event
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.common.field_email_model import FieldEmailModel
from gui.impl.lobby.account_completion.common import errors
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.account_completion.common.base_field_model import BaseFieldModel
_EMAIL_PATTERN = re.compile(b'^[a-z0-9_-]+(\\.[a-z0-9_-]+)*@([a-z0-9]([a-z0-9-]*[a-z0-9])?\\.)+[a-z]{2,4}$', re.I)

class BaseFieldPresenter(object):
    __metaclass__ = ABCMeta
    __slots__ = (b'_value', b'_viewModel', b'onValueChanged', b'onFocusLost')

    def __init__(self, viewModel):
        super(BaseFieldPresenter, self).__init__()
        viewModel.onChange += self.__valueChangeHandler
        viewModel.onLostFocus += self.__lostFocusChangeHandler
        self._value = b''
        self._viewModel = viewModel
        self.onValueChanged = Event()
        self.onFocusLost = Event()
        return

    @property
    def viewModel(self):
        return self._viewModel

    @property
    def value(self):
        return self._value

    @property
    def isValid(self):
        return not self._viewModel.getErrorMessage()

    def clear(self):
        self.setValue(b'')
        self.viewModel.setErrorMessage(b'')
        return

    def setValue(self, value):
        self._value = value
        self.viewModel.setValue(value)
        return

    def dispose(self):
        self._viewModel.onChange -= self.__valueChangeHandler
        self._viewModel.onLostFocus -= self.__lostFocusChangeHandler
        self._viewModel = None
        return

    def validate(self):
        self._validateChangedValue()
        if self.isValid:
            self._validateValueWhenFocusChanged()
        return self.isValid

    @abstractmethod
    def _validateChangedValue(self):
        raise NotImplementedError
        return

    @abstractmethod
    def _validateValueWhenFocusChanged(self):
        raise NotImplementedError
        return

    def __valueChangeHandler(self, args):
        self._value = args.get(b'value', b'')
        self._validateChangedValue()
        self.onValueChanged()
        return

    def __lostFocusChangeHandler(self):
        if self.isValid and self._value:
            self._validateValueWhenFocusChanged()
        self.onFocusLost()
        return


class EmailPresenter(BaseFieldPresenter):
    __slots__ = ()

    def __init__(self, viewModel):
        super(EmailPresenter, self).__init__(viewModel)
        self.viewModel.setName(R.strings.dialogs.accountCompletion.email.fieldName())
        self.viewModel.setPlaceholder(backport.text(R.strings.dialogs.accountCompletion.email.fieldPlaceholder()))
        return

    @property
    def viewModel(self):
        return self._viewModel

    def _validateChangedValue(self):
        with self.viewModel.transaction() as vm:
            vm.setErrorTime(0)
            if len(self._value) > FieldEmailModel.EMAIL_LEN_MAX:
                vm.setErrorMessage(errors.emailIsTooLong())
            else:
                vm.setErrorMessage(b'')
        return

    def _validateValueWhenFocusChanged(self):
        if len(self._value) < FieldEmailModel.EMAIL_LEN_MIN:
            self.viewModel.setErrorMessage(errors.emailIsTooShort())
        elif not _EMAIL_PATTERN.match(self._value):
            self.viewModel.setErrorMessage(errors.emailIsInvalid())
        return


class CodePresenter(BaseFieldPresenter):
    __slots__ = ()

    def _validateChangedValue(self):
        self.viewModel.setErrorMessage(b'')
        return

    def _validateValueWhenFocusChanged(self):
        return
