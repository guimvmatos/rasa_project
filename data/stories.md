## iniciando_chat_happy_path
* get_started
  - aluno_form
  - form{"name": "aluno_form"}
  - form{"name": null}
  - dadosAluno
  - utter_offer_options

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

## pedido declaracao de matricula
* declaracao_matricula
  - utter_declaracao_matricula
  - utter_what_more

## out of scope
* out_of_scope
  - utter_out_of_scope
  - utter_offer_options

  ## bot challenge
* bot_challenge
  - utter_iamabot
