# AWS Step Functions - Fluxo de Processamento de Pedidos

Este projeto simula um fluxo de trabalho de processamento de pedidos usando AWS Step Functions. O fluxo de trabalho realiza as seguintes etapas:

1. **Check Inventory**: Verifica a disponibilidade do item no estoque.
2. **Process Payment**: Simula o pagamento do pedido.
3. **Update Order Status**: Atualiza o status do pedido para "Confirmado".
4. **Notify Customer**: Envia uma confirmação ao cliente.

## Como Executar

1. **Configurar as Funções Lambda**: Faça o upload de cada script Python da pasta `src/` para a AWS Lambda.
2. **Criar o Workflow no Step Functions**: Use o arquivo `order_processing_workflow.json` para definir o fluxo de trabalho.
3. **Executar o Workflow**: Inicie uma execução e monitore o progresso em Step Functions.

## Tecnologias Utilizadas

- **AWS Step Functions**
- **AWS Lambda**
- **Amazon States Language (ASL)**
