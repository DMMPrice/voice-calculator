from infix_eval import evaluate as ev


def operator_re(stack_op):
    for i in range(0, len(stack_op)):
        if stack_op[i] == "to the power":
            stack_op.insert(i, '**')
            stack_op.remove('to the power')
    for i in range(0, len(stack_op)):
        if stack_op[i] == "by":
            stack_op.insert(i, '/')
            stack_op.remove('by')
    for i in range(0, len(stack_op)):
        if stack_op[i] == "into":
            stack_op.insert(i, '*')
            stack_op.remove('into')
    for i in range(0, len(stack_op)):
        if stack_op[i] == "x":
            stack_op.insert(i, '*')
            stack_op.remove('x')
    return stack_op


def one_replacement(stack_op):
    for i in range(0, len(stack_op)):
        if stack_op[i] == 'oneplus':
            stack_op.insert(i, '1')
            stack_op.insert(i + 1, '+')
            stack_op.remove('oneplus')
    for i in range(0, len(stack_op)):
        if stack_op[i] == 'one':
            stack_op.insert(i, '1')
            stack_op.remove('one')
    return stack_op


def refine_voice(stack_op):
    refine_string = ''
    for i in range(0, len(stack_op)):
        refine_string += stack_op[i] + ' '
    return refine_string


def voice_input():
    import speech_recognition as s_r
    r = s_r.Recognizer()
    my_mic_device = s_r.Microphone(device_index=1)
    with my_mic_device as source:
        print("Say what you want to calculate, example: 3 plus 3")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        my_string = r.recognize_google(audio)
        # print(type(my_string))
    return my_string.lower()


def main_function():
    voice = voice_input()
    print(voice)
    test_list = voice.split(' ')
    test_list_1 = one_replacement(test_list)
    test_list_2 = operator_re(test_list_1)
    test_str = refine_voice(test_list_2)
    print(ev(test_str))


main_function()

# test_input = '2 into 4'
# test_list = test_input.split(' ')
# # print(test_list)
