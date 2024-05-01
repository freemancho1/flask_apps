import warnings
from sklearn.exceptions import DataConversionWarning
from sklearn.exceptions import ConvergenceWarning


class AppInit:
    def __init__(self) -> None:
        self._run()
        
    def _run(self) -> None:
        self._set_warnings()
        
    def _set_warnings(self) -> None:
        # Warning(can be ignored) that may occur when reading Excel file data
        module = 'openpyxl.styles.stylesheet'
        warnings.filterwarnings('ignore', category=UserWarning, module=module)
        
        warnings.filterwarnings(action='ignore', category=DataConversionWarning)
        warnings.filterwarnings(action='ignore', category=ConvergenceWarning)
        warnings.filterwarnings(action='ignore', category=FutureWarning)