# TODO
- [ ] microsservicos
    - [ ] servico cadastramento
        - [ x ] script inicialização
        - [ x ] GET /servcad/clientes
        - [ x ] GET /servcad/aplicativos
        - [ x ] POST /servcad/assinaturas
        - [ x ] PATCH /servcad/aplicativos/:idAplicativo
        - [ x ] GET /servcad/assinaturas/{tipo}
        - [ x ] GET /servcad/asscli/:codcli
        - [ x ] GET /servcad/assapp/:codapp
        - [ ] evento: PagamentoServicoCadastramento
            - [ ] event handler
    - [ ] servico pagamentos
        - [ ] POST /registrarpagamento
        - [ ] evento: PagamentoServicoCadastramento
            - [ ] event handler
        - [ ] evento: PagsmentoServicoAssinaturaValida
            - [ ] event handler
    - [ ] servico assinaturas validas
        - [ ] GET /assinvalidas/:codass
        - [ ] evento: PagamentoServicoAssinaturaValida
            - [ ] event handler

- [ ] entrega
    - [ ] diagrama entidade-relacionamento banco de dados
    - [ ] diagramas de componentes
    - [ ] diagramas de implantação

    - [ ] passo a passo para implantação do sistema

    - [ ] vídeo demonstrando a execução do sistema em uma plataforma nuvem 

- [ ] fazer deploy dos 3 microsservicos distintos
    - [ ] cadastramento
    - [ ] pagamentos
    - [ ] assinaturas

decidir entre: aws ou azure?
confirmar com o sor se pode ser mongo mas com ids de relação entre eles.... - email ou achamos com ele algum dia?
 

## entidades de domínio
![alt text](image.png)

## arquitetura do sistema
![alt text](image-1.png)