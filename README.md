# sistemagppp
Sistema de Gerenciamento de Pedidos com Padrões de Projeto

Projeto: Sistema de Gerenciamento de Pedidos com Padrões de Projeto
1. Objetivo
Desenvolver um sistema que gerencie pedidos de uma loja online, aplicando padrões de projeto de forma incremental. O sistema deve ter uma estrutura modular, testes automatizados e documentação técnica clara.
2. Padrões Utilizados e Justificativa
Criacionais
- Builder: Facilita a criação de pedidos com múltiplos atributos opcionais.
- Singleton: Garante que o sistema de gerenciamento de pedidos tenha uma única instância global.
Estruturais
- Facade: Oferece uma interface unificada para gerenciar pedidos, clientes e pagamentos.
- Adapter: Permite integração com diferentes gateways de pagamento.
Comportamentais
- Observer: Notifica os clientes quando há mudanças no status do pedido.
- Strategy: Permite diferentes estratégias de cálculo de frete (normal, expresso, internacional).
- State: Gerencia o estado do pedido, como "Em processamento", "Enviado" e "Entregue".

3. Implementação
Aqui está um exemplo inicial do código em Python, aplicando alguns padrões:

# Singleton - Gerenciador de Pedidos
class OrderManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
            cls._instance.orders = []
        return cls._instance

    def add_order(self, order):
        self.orders.append(order)

    def list_orders(self):
        return self.orders

# Builder - Construção de Pedidos
class OrderBuilder:
    def __init__(self):
        self.order = {}

    def add_customer(self, name):
        self.order["customer"] = name
        return self

    def add_product(self, product):
        if "products" not in self.order:
            self.order["products"] = []
        self.order["products"].append(product)
        return self

    def set_shipping(self, shipping_type):
        self.order["shipping"] = shipping_type
        return self

    def build(self):
        return self.order

# Uso do Builder
order = OrderBuilder().add_customer("Eduardo").add_product("Laptop").set_shipping("Expresso").build()
print(order)

# Strategy - Cálculo de Frete
class ShippingStrategy:
    def calculate(self, distance):
        pass

class NormalShipping(ShippingStrategy):
    def calculate(self, distance):
        return distance * 1.0

class ExpressShipping(ShippingStrategy):
    def calculate(self, distance):
        return distance * 2.0

class InternationalShipping(ShippingStrategy):
    def calculate(self, distance):
        return distance * 3.0

class ShippingContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate_shipping(self, distance):
        return self.strategy.calculate(distance)

# Uso do Strategy
shipping = ShippingContext(ExpressShipping())
print(shipping.calculate_shipping(100))  # Output: 200

4. Testes Unitários
Exemplo de teste para o Singleton:

import unittest

class TestOrderManager(unittest.TestCase):
    def test_singleton_instance(self):
        manager1 = OrderManager()
        manager2 = OrderManager()
        self.assertIs(manager1, manager2)  # Ambas as instâncias devem ser iguais
		
5. Documentação
Como foi implementado:
- Singleton garante que haja uma única instância do gerenciador de pedidos.
- Builder simplifica a criação de pedidos de forma flexível.
- Strategy permite diferentes métodos de cálculo de frete.
- State pode ser implementado para gerenciar os diferentes estados de um pedido.
- Observer pode notificar o cliente sobre mudanças no status do pedido.

Esse modelo está mais robusto e flexível para uma aplicação real. Gostaria que eu adicionasse mais detalhes ou novos padrões? 🚀
