# import english
# import exchange
import notion


if __name__ == '__main__':
    # english.addTrans()
    # exchange.get_exchange()

    # notion:
    pdf_path = "AWS Certified Cloud Practitioner CLF-C02.pdf"
    total_question_number = 2
    for question_number in range(1, (total_question_number + 1)):
        options = notion.extract_options_from_pdf(pdf_path, question_number)
        notion.write_txt(options, question_number)
        print(f"{question_number} is written.")