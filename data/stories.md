## iniciando_chat_happy_path
* get_started
  - aluno_form
  - form{"name": "aluno_form"}
  - form{"name": null}
  - dadosAluno
  - utter_device


## iniciando_chat_unhappy_path
* greet
  - aluno_form
  - form{"name": "aluno_form"}
  - form{"name": null}
  - dadosAluno
  - utter_device

## acesso pelo celular_afirmativa
* smartphone
  - utter_smartphone_advice
* afirmativa
  - utter_acesso_unifeb_digital_com_link

## acesso_celular_negativa
* smartphone
  - utter_smartphone_advice
* negativa
  - utter_goodbye

## acesso_computer_happy_path
* computer
  - utter_acesso_unifeb_digital_com_link
* afirmativa
  - utter_goodbye

## acesso_computer_unhappy_path
* computer
  - utter_acesso_unifeb_digital_com_link
* negativa
  - utter_ask_problems

## acesso_unifeb_digital_com_link_problem_myemail
* myemail
  - utter_your_email
  - utter_acesso_unifeb_digital_com_link

## acesso_unifeb_digital_com_link_problem_fluigpassword_happy_path
* fluigpassword
  - utter_fluigpassword
* afirmativa
  - utter_acesso_unifeb_digital_com_link

## acesso_unifeb_digital_com_link_problem_fluigpassword_unhappy_path
* fluigpassword
  - utter_fluigpassword
* negativa
  - utter_relacionamento

## acesso_unifeb_digital_com_link_problem_fulltutorial_happy_path
* fulltutorial
  - utter_fulltutorial
* afirmativa
  - utter_goodbye

## acesso_unifeb_digital_com_link_problem_fulltutorial_unhappy_path_detail
* fulltutorial
  - utter_fulltutorial
* negativa
  - utter_ask_tutorials

## tutorial_detalhado
* detailtutorial
  - utter_detail_tutorial_1

## relacionamento
* relacionamento
  - utter_relacionamento

## pedido de boleto_happy_path_outros
* boleto
  - enviarBoleto
  - utter_boleto
* afirmativa
  - utter_what_more
* afirmativa
  - utter_offer_options

## pedido de boleto_happy_path
* boleto
  - enviarBoleto
  - utter_boleto
* afirmativa
  - utter_what_more
* negativa
  - utter_goodbye

## pedido de boleto_unhappy_path
* boleto
  - enviarBoleto
  - utter_boleto
* relacionamento
  - utter_relacionamento

## pedido declaracao de matricula aluno
* declaracao_matricula
  - utter_declaracao_matricula
* aluno
  - utter_declaracao_matricula_aluno
  - utter_what_more

## pedido declaracao de matricula ex-aluno
* declaracao_matricula
  - utter_declaracao_matricula
* exaluno
  - utter_declaracao_matricula_exaluno
  - utter_what_more

## out of scope
* out_of_scope
  - utter_out_of_scope
  - utter_offer_options

  ## bot challenge
* bot_challenge
  - utter_iamabot
