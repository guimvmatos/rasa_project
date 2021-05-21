## iniciando_chat_server_side_unhappy_path
* get_started
  - aluno_form
  - form{"name": "aluno_form"}
  - form{"name": null}
  - dadosAluno
  - utter_begins
* relacionamento
  - utter_relacionamento
  - handoverAction

## iniciando_chat_server_side_happy_path
* get_started
  - aluno_form
  - form{"name": "aluno_form"}
  - form{"name": null}
  - dadosAluno
  - utter_begins
* avalIntegradora
  - utter_device


## iniciando_chat_user_side_unhappy_path
* greet
  - aluno_form
  - form{"name": "aluno_form"}
  - form{"name": null}
  - dadosAluno
  - utter_begins
* relacionamento
  - utter_relacionamento
  - handoverAction

## iniciando_chat_user_side_happy_path
* greet
  - aluno_form
  - form{"name": "aluno_form"}
  - form{"name": null}
  - dadosAluno
  - utter_begins
* avalIntegradora
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

## acesso_computer_happy_path_corret_exam
* computer
  - utter_acesso_unifeb_digital_com_link
* afirmativa
  - utter_confirmation
* afirmativa
  - utter_goodbye

## acesso_computer_happy_path_incorrect_exam
* computer
  - utter_acesso_unifeb_digital_com_link
* afirmativa
  - utter_confirmation
* relacionamento
  - utter_relacionamento
  - handoverAction

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
  - handoverAction

## acesso_unifeb_digital_com_link_problem_portalpassword_happy_path
* portalpassword
  - utter_portalpassword
* afirmativa
  - utter_acesso_unifeb_digital_com_link

## acesso_unifeb_digital_com_link_problem_portalpassword_unhappy_path
* portalpassword
  - utter_portalpassword
* relacionamento
  - utter_relacionamento
  - handoverAction

## acesso_unifeb_digital_com_link_problem_fulltutorial_happy_path_correct_exam
* fulltutorial
  - utter_fulltutorial
* afirmativa
  - utter_confirmation
* afirmativa
  - utter_goodbye

## acesso_unifeb_digital_com_link_problem_fulltutorial_unhappy_path_detail
* fulltutorial
  - utter_fulltutorial
* negativa
  - utter_ask_tutorials

## tutorial_detalhado_happy_path
* detailtutorial
  - utter_detail_tutorial_1
  - utter_detail_tutorial_1.1
* afirmativa
  - utter_detail_tutorial_2
  - utter_detail_tutorial_2.1
* afirmativa
  - utter_detail_tutorial_3
  - utter_detail_tutorial_3.1
* afirmativa
  - utter_detail_tutorial_4
  - utter_detail_tutorial_4.1
* afirmativa
  - utter_detail_tutorial_5
  - utter_detail_tutorial_5.1
* afirmativa
  - utter_detail_tutorial_6
  - utter_detail_tutorial_6.1
* afirmativa
  - utter_confirmation
* afirmativa
  - utter_goodbye

## tutorial_detalhado_unhappy_path_tutorial_1
* detailtutorial
  - utter_detail_tutorial_1
  - utter_detail_tutorial_1.1
* relacionamento
  - utter_relacionamento
  - handoverAction

## tutorial_detalhado_unhappy_path_tutorial_2_a
* detailtutorial
  - utter_detail_tutorial_1
  - utter_detail_tutorial_1.1
* afirmativa
  - utter_detail_tutorial_2
  - utter_detail_tutorial_2.1
* myemail
  - utter_your_email
  - utter_detail_tutorial_2
  - utter_detail_tutorial_2.1

## tutorial_detalhado_unhappy_path_tutorial_2_b
* detailtutorial
  - utter_detail_tutorial_1
  - utter_detail_tutorial_1.1
* afirmativa
  - utter_detail_tutorial_2
  - utter_detail_tutorial_2.1
* fluigpassword
  - utter_fluigpassword

## tutorial_detalhado_unhappy_path_tutorial_3
* detailtutorial
  - utter_detail_tutorial_1
  - utter_detail_tutorial_1.1
* afirmativa
  - utter_detail_tutorial_2
  - utter_detail_tutorial_2.1
* afirmativa
  - utter_detail_tutorial_3
  - utter_detail_tutorial_3.1
* relacionamento
  - utter_relacionamento
  - handoverAction

## tutorial_detalhado_happy_path_tutorial_4
* detailtutorial
  - utter_detail_tutorial_1
  - utter_detail_tutorial_1.1
* afirmativa
  - utter_detail_tutorial_2
  - utter_detail_tutorial_2.1
* afirmativa
  - utter_detail_tutorial_3
  - utter_detail_tutorial_3.1
* afirmativa
  - utter_detail_tutorial_4
  - utter_detail_tutorial_4.1
* portalpassword
  - utter_portalpassword
* relacionamento
  - utter_relacionamento
  - handoverAction

## tutorial_detalhado_happy_path_tutorial_5
* detailtutorial
  - utter_detail_tutorial_1
  - utter_detail_tutorial_1.1
* afirmativa
  - utter_detail_tutorial_2
  - utter_detail_tutorial_2.1
* afirmativa
  - utter_detail_tutorial_3
  - utter_detail_tutorial_3.1
* afirmativa
  - utter_detail_tutorial_4
  - utter_detail_tutorial_4.1
* afirmativa
  - utter_detail_tutorial_5
  - utter_detail_tutorial_5.1
* relacionamento
  - utter_relacionamento
  - handoverAction

## tutorial_detalhado_happy_path_tutorial_6
* detailtutorial
  - utter_detail_tutorial_1
  - utter_detail_tutorial_1.1
* afirmativa
  - utter_detail_tutorial_2
  - utter_detail_tutorial_2.1
* afirmativa
  - utter_detail_tutorial_3
  - utter_detail_tutorial_3.1
* afirmativa
  - utter_detail_tutorial_4
  - utter_detail_tutorial_4.1
* afirmativa
  - utter_detail_tutorial_5
  - utter_detail_tutorial_5.1
* afirmativa
  - utter_detail_tutorial_6
  - utter_detail_tutorial_6.1
* relacionamento
  - utter_relacionamento
  - handoverAction

## relacionamento
* relacionamento
  - utter_relacionamento
  - handoverAction

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
  - handoverAction

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
