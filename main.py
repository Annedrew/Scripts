# import english
# import exchange
# import pdf_extract_aws
import movie_scraping


if __name__ == '__main__':
    # english.addTrans()
    # exchange.get_exchange()

    # pdf_extract_aws:
    # pdf_path = "AWS Certified Cloud Practitioner CLF-C02(1-5pages).pdf"
    # start_question_number = 624
    # end_question_number = 669
    # for question_number in range(start_question_number, (end_question_number + 1)):
    #     options = pdf_extract_aws.extract_options_from_pdf(pdf_path, question_number)
    #     pdf_extract_aws.write_txt(options, question_number)
    #     print(f"{question_number} is written.")

    # movie_scraping
    web_url = "https://www.rottentomatoes.com/"
    movie_scraping.access_page(web_url)