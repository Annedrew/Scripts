# import english
# import exchange
import notion


if __name__ == '__main__':
    # english.addTrans()
    # exchange.get_exchange()

    # notion:
    pdf_path = "AWS Certified Cloud Practitioner CLF-C02(1-5pages).pdf"
    start_question_number = 624
    end_question_number = 669
    for question_number in range(start_question_number, (end_question_number + 1)):
        options = notion.extract_options_from_pdf(pdf_path, question_number)
        notion.write_txt(options, question_number)
        print(f"{question_number} is written.")