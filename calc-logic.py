import speech_recognition as s_r
import operator

r = s_r.Recognizer()
my_mic_device = s_r.Microphone(device_index=1)


# print all the microphones connected to your machine
# print(s_r.Microphone.list_microphone_names())
def operator_re(test_string):
    if test_string.find('x') > 0:
        test_string.replace("x", "*")
        return test_string
    if test_string.find('to the power') > 0:
        test_string.replace("to the power", "*")
        return test_string
    if test_string.find('into') > 0:
        test_string.replace("into", "*")
        return test_string
    else:
        return test_string


with my_mic_device as source:
    print("Say what you want to calculate, example: 3 plus 3")
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)
    my_string = r.recognize_google(audio)
    # print(type(my_string))

my_string = my_string.lower()


# print(my_string)
# print(my_string.replace("into", "*"))
# print('The changed string is')
# changed_str = operator_re(my_string)
# print(changed_str)

def get_operator_fn(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        'into': operator.mul,
        'multiplied by': operator.mul,
        'x': operator.mul,
        'divided': operator.__truediv__,
        'by': operator.__truediv__,
        'Mod': operator.mod,
        'mod': operator.mod,
        '^': operator.xor,
    }[op]


def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


print(eval_binary_expr(*(my_string.split())))
