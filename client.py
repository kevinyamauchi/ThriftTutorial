import sys, glob

# Add the generated python files to the path
sys.path.append('gen-py')
#sys.path.insert(0, glob.glob('./thrift/lib/py/build/lib.*')[0])

from tutorial import Calculator
from tutorial.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is required because the socket is slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Calculator.Client(protocol)

    # Connect
    transport.open()

    client.ping()
    print 'ping()'

    # Try simple addition
    sum = client.add(1, 1)
    print '1 + 1 = %d' % (sum)

    work = Work()
    work.op = Operation.DIVIDE
    work.num1 = 1
    work.num2 = 0

    try:
        quotient = client.calculate(1, work)
        print 'You divided by zero...'

    except InvalidOperation, io:
        print 'InvalidOperation: %r' % io

    work.op = Operation.SUBTRACT
    work.num1 = 15
    work.num2 = 10

    diff = client.calculate(1, work)
    print '15 - 10 = %d' % (diff)

    log = client.getStruct(1)
    print 'Check log: %s' % (log.value)

    # Close the connection
    transport.close()

except Thrift.TException, tx:
    print '%s' % (tx.message)


