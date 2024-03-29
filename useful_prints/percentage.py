try:
    from to_precision import std_notation
except:
    raise ImportError(
        "'to_precision' could not be imported please make sure you installed it.\n\tLink to GitHub rep: https://github.com/BebeSparkelSparkel/to-precision\n\tLink to Bitbucket: https://bitbucket.org/william_rusnack/to-precision/src/master/"
    )

from colorful_terminal import *
from exception_details import print_exception_details


def get_percentage_as_fitted_string(
    count: int, total: int, round_to: int = 2, with_percentage_symbol: bool = True
):
    perc = count / total * 100
    if perc < 0.01:
        perc = "  " + str(std_notation(perc, -2 + round_to))
    elif perc < 0.1:
        perc = "  " + str(std_notation(perc, -1 + round_to))
    elif perc < 1:
        perc = "  " + str(std_notation(perc, 0 + round_to))
    elif perc < 10:
        perc = "  " + str(std_notation(perc, 1 + round_to))
    elif perc < 100:
        perc = " " + str(std_notation(perc, 2 + round_to))
    else:
        perc = str(std_notation(perc, 3 + round_to))
    if with_percentage_symbol:
        perc += " %"
    return perc


def progress_printer(
    count: int, total: int, pre_string: str = "Progress: ", post_string: str = ""
):
    TermAct.clear_current_line_action()
    print(
        f"{pre_string}{count} / {total}    ({get_percentage_as_fitted_string(count, total)}){post_string}",
        end="",
    )
    if count == total:
        print()


def main_and_sub_progress_printer(
    maincount: int,
    maintotal: int,
    subcount: int,
    subtotal: int,
    pre_string: str = "Progress: ",
    mainpre_string: str = "Main-Progress: ",
    subpre_string: str = "Sub-Progress: ",
    post_string: str = "",
    mainpost_string: str = "",
    subpost_string: str = "",
):
    if maincount == 0 and subcount == 0:
        print(TermAct.hide_cursor(), end="")

    if post_string == "":
        lines = 3
    else:
        lines = 4 + post_string.count("\n")
    if maincount != 0 and subcount != 0:
        for i in range(lines):
            colored_print(TermAct.cursor_previous_line, end="")

    try:
        print(f"{pre_string}")
        print(
            f"{mainpre_string}{maincount} / {maintotal}    ({get_percentage_as_fitted_string(maincount, maintotal)}){mainpost_string}"
            + TermAct.erase_in_line()
        )
        print(
            f"{subpre_string}{subcount} / {subtotal}    ({get_percentage_as_fitted_string(subcount, subtotal)}){subpost_string}"
            + TermAct.erase_in_line()
        )
        if post_string != "":
            print(post_string)
    except Exception as e:
        print("\n" * 20)
        print_exception_details(e)
        print("\n" * 20)
    if maincount == maintotal and subcount == subtotal:
        print(TermAct.show_cursor(), end="")
