from python_project.extra_broker import Backtest
from pybacktestchain.broker import StopLoss
from pybacktestchain.blockchain import load_blockchain


# Set verbosity for logging
verbose = False  # Set to True to enable logging, or False to suppress it

backtest = Backtest(risk_model=StopLoss,
    name_blockchain='backtest',
    verbose=verbose)


backtest.run_backtest()

block_chain = load_blockchain('backtest')
print(str(block_chain))
# check if the blockchain is valid
print(block_chain.is_valid())