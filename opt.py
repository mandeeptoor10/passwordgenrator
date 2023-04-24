import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symols=[!,@,#,$,%,^,&,*,(,),_,+,=,-,:,:,',,,.,/,*,-,+,.,]

def generate_opt():
    password = ""
    for i in range(random.randint(8, 16)):
        password += str(random.choice(numbers + capitals + small_alphabets))
    return password
print(generate_opt())
