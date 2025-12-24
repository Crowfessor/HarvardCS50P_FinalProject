from project import Student, StudentRegister
import os

def test_add_student():
    register = StudentRegister("test_add.csv")

    student = Student('123' , 'John', 'Wick', 'Computer Science', '85')
    register.add(student)


    check = register.search('123')
    assert check is not None
    assert check.firstname == 'John'
    assert check.lastname == 'Wick'
    assert check.classroom == 'Computer Science'
    assert check.grade == '85'

    if os.path.exists("test_add.csv"):
        os.remove("test_add.csv")

def test_remove_student():

    register = StudentRegister("test_remove.csv")

    student = Student('99999', 'Agent', 'Smith', 'Chemistry', '90')
    register.add(student)

    assert register.search('99999') is not None

    result1 = register.remove('99999')
    assert result1 == True
    assert register.search('99999') is None

    result2 = register.remove('99999')
    assert result2 == False

    if os.path.exists("test_remove.csv"):
        os.remove("test_remove.csv")

def test_search_student():

    register = StudentRegister("test_search.csv")
    
    student1 = Student('111', 'Bob', 'Bobson', 'Physics', '75')
    student2 = Student('222', 'Emma', 'Watson', 'Chemistry', '88')
    student3 = Student('333', 'Charlize', 'Theron', 'Biology', '92')
    
    register.add(student1)
    register.add(student2)
    register.add(student3)
    
    found1 = register.search('111')
    assert found1 is not None
    assert found1.firstname == 'Bob'
    
    found2 = register.search('222')
    assert found2 is not None
    assert found2.lastname == 'Watson'
    
    not_found = register.search('999')
    assert not_found is None
    
    if os.path.exists("test_search.csv"):
        os.remove("test_search.csv")