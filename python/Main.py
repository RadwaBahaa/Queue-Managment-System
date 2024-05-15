from Child import ChildQueue, QueueOutOfRangeException

# Edit the queue
def editqueue():
    while True:
        try:
            question2 = int(input("""\n__________What do you want to do?
            1- Add data the queue
            2- Pop data from the queue
            3- End..."""))
            try:
                if question2 == 1:
                    addingdata()
                elif question2 == 2:
                    popdata()
                elif question2 == 3:
                    break
                elif question2 < 1 or question2 > 3:
                    print('Invalid answer --> It must be between 1 and 3')
            except:
                print('There was an error --> There is no any queue')
                break
        except:
            print('Invalid answer --> It must be between 1 and 3')
# Adding data to the queue
def addingdata():
    print(f'\n_____ Adding Data to the queue {queuename}_____')
    def addingsyntax():
        global queue
        queue.insert(input('Enter more data: '))
        print(queue.getqueue(queuename))
    addingsyntax()
    while True:
        try:
            add = input('\nDo you want to add another data?  y/n').lower()
            if add == 'y':
                addingsyntax()
            elif add == 'n':
                print('End adding operation')
                break
            else:
                print('Invalid answer')
        except QueueOutOfRangeException as error:
            print(f'_____{error}_____')
            break
# Pop data from the queue
def popdata():
    print(f'\n_____ Pop Data from the queue {queuename}_____')
    def popsyntax():
        print('The deleted data is: ', queue.pop())
        print('___The queue after deleting___\n', queue.getqueue(queuename), '\n')
    popsyntax()
    while True:
        try:
            pop = input(f'\nDo you want to pop data from the queue {queuename}?  y/n  ').lower()
            if pop == 'y':
                if queue.is_empty() == False:
                    popsyntax()
                    pass
            elif pop == 'n':
                print('__End pop operation__')
                queue.update(queuename)
                break
            else:
                print('__Invalid answer__')
        except QueueOutOfRangeException as error:
            print(f'_____{error}_____')
            break
# Delete a specific queue
def deletedata():
     try:
         ChildQueue.empty()
         name = input('\nEnter the name of the queue you want to delete: ')
         print(f'\n_____ Delete data of the queue {name}_____')
         queue.deletequeue(name)
         print(queue.load())
     except Exception as error:
         print(f'_____{error}_____')
# Delete all the queues
def deleteallqueues():
    try:
        ChildQueue.empty()
        print(queue.deleteallqueues())
    except Exception as error:
        print(f'_____{error}_____')
# Display data of an existing queue
def displayqueue():
    try:
        ChildQueue.empty()
        name = input('Enter the queue name: ').upper()
        print(queue.getqueue(name))
    except Exception as error:
        print(f'_____{error}_____')

# Display all queues
def displayallqueues():
    try:
        print(ChildQueue.load())
    except Exception as error:
        print(f'_____{error}_____')

if __name__ == '__main__':
    print('\n\n___________Welcome ^_^___________')
    queuename = ''
    queuesize = 0

    while True:
        try:
            question1 = int(input("""\nWhat do you want to do?(inter the number of operation)__  
            1- Create a new queue
            2- Display an existing queue
            3- Delete an existing queue
            4- Display all existing queues
            5- Delete all existing queues
            6- End..."""))

            if question1 == 1:
                print('Creating a Queue_____')
                while True:
                    try:
                        queuename = input('\nEnter the name of the queue: ').upper()
                        queuesize = input('Enter the size of the queue (more than 0): ')
                        queue = ChildQueue(queuename, queuesize)  # Creating the queue with a name and size
                        print(queue.getqueue(queuename))
                        editqueue()
                        break
                    except Exception as error:
                        print(f'_____{error}_____')
            elif question1 == 2:
                displayqueue()
            elif question1 == 3:
                deletedata()
            elif question1 == 4:
                displayallqueues()
            elif question1 == 5:
                deleteallqueues()
            elif question1 == 6:
                print('__________________ Thanks __________________')
                break

        except ValueError:
            print('Invalid answer --> It must be an integer between 1 and 6')








