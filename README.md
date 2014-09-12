ThriftTutorial
==============

This is the Thrift tutorial from http://thrift.apache.org/tutorial/.

I generated the python scripts using:

```
thrift -r --gen py tutorial.thrift
```

The client and server scripts assume that they are in the ThriftTutorial directory. Additionally the Thrift Python bindings must be installed. I installed them through pip.

```
sudo pip install thrift

```

I had to add the thrift source folder to  the ThriftTutorial directory to add the libraries...I need to find where pip installed them...I changed the path insert to

```
sys.path.insert(0, glob.glob('./thrift/lib/py/build/lib.*')[0])

```

First, I started the server and received the following output

```
Starting the server...

```

Note that there is no confirmation that the server has in fact started. Next, I ran the client script (client.py) and received the following output

```
ping()
1 + 1 = 2
InvalidOperation: InvalidOperation(what=4, why='Cannot divide by 0')
15 - 10 = 5
Check log: 5

```

The server gave the following output

```
ping()
add(1, 1)
calculate(1, Work(comment=None, num1=1, num2=0, op=4))
calculate(1, Work(comment=None, num1=15, num2=10, op=2))
getStruct(1)

```

