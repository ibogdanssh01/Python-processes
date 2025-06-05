from enum import Enum, IntFlag, auto

class ProcessType(Enum):
    """
    Represents the types of Processes during the scan.

    ### Members
    - 'PROCESS_CATEGORY_APP'            -- Programs running in the background that typically provide services.
    - 'PROCESS_CATEGORY_BACKGROUND'     -- Applications you've launched yourself, like a web browser or text editor.
    - 'PROCESS_CATEGORY_WINDOWS_SYSTEM' -- Core system processes necessary for Windows to function, e.g., 'csrss.exe', 'svchost.exe'
    - 'PROCESS_CATEGORY_OTHER'          -- For unclassified processes
    """

    PROCESS_CATEGORY_APP            = "PROCESS_CATEGORY_APP"
    PROCESS_CATEGORY_BACKGROUND     = "PROCESS_CATEGORY_BACKGROUND"
    PROCESS_CATEGORY_WINDOWS_SYSTEM = "PROCESS_CATEGORY_WINDOWS_SYSTEM"
    PROCESS_CATEGORY_OTHER          = "PROCESS_CATEGORY_OTHER"
