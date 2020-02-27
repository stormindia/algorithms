arr = [1,2,3,4,5,'abc', 8.5, 0]

for i in arr:
    try:
        print(1/i)
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except:
        print('unknown error')
