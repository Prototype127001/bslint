import sys
import src
import glob
import Constants as const


def run(file):
    file_reader = src.FileReader()
    result = file_reader.read_file(file)
    lexer = src.Lexer(result[2])
    if result[0]:
        print(result[0])

    lex_result = lexer.lex(result[1])
    print(const.HEADER_COLOUR + filename + const.END_COLOUR)
    if lex_result["Status"] == "Error":
        for error in lex_result["Tokens"]:
            print(const.ERROR_COLOUR + "Error at line number:  " +
                  str(error[1]) + const.END_COLOUR)

        for warning in lex_result["Warnings"]:
            print(const.WARNING_COLOUR + str(warning) + const.END_COLOUR)
        if not lex_result["Warnings"]:
            print(const.PASS_COLOUR + "Lexed without warnings" + const.END_COLOUR)
    else:
        print(const.PASS_COLOUR + filename + "Lexed without errors" + const.END_COLOUR)
        for warning in lex_result["Warnings"]:
            print(const.WARNING_COLOUR + str(warning) + const.END_COLOUR)
        if not lex_result["Warnings"]:
            print(const.PASS_COLOUR + "Lexed without warnings" + const.END_COLOUR)

    print("\n")


if __name__ == '__main__':
    for filename in glob.iglob(sys.argv[1] + '/**/*.brs', recursive=True):
        run(filename)
        # print(filename)
        # run(sys.argv[1])