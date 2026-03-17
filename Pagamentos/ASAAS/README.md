### Gerador de PIX Estatico sem Verificação 
```php
Route::get('/', function () {
    $client = new Client();
    $response = $client->post('https://api.asaas.com/v3/pix/qrCodes/static', [
        'headers' => [
            'accept' => 'application/json',
            'access_token' => env('ASAAS_TOKEN'),
            'content-type' => 'application/json',
        ],
        'json' => [
            "format" => "IMAGE",
            "value" => 2,
            "description" => "Pagamento por PIX",
            "addressKey" => "00c0969d-f144-4e82-8fa2-fa9df928fc70"
        ]
    ]);
    $qrData = json_decode($response->getBody(), true);
    return view('pix', [
        'qr' => $qrData
    ]);
});
```

### Gerador de PIX Dinâmico  
```php
Route::get('/pix', function () {
    $client = new Client();
    $valor = 5;
    $response = $client->post('https://api.asaas.com/v3/payments', [
        'headers' => [
            'accept' => 'application/json',
            'access_token' => env('ASAAS_TOKEN'),
            'content-type' => 'application/json',
        ],
        'json' => [
            "billingType" => "PIX",
            "customer" => "cus_0007898785621351",
            "value" => $valor,
            "dueDate" => date('Y-m-d', strtotime('+1 day')),
            "description" => "Pagamento Pix"
        ]
    ]);
    $payment = json_decode($response->getBody(), true);
    $paymentId = $payment['id'];
    $qrResponse = $client->get("https://api.asaas.com/v3/payments/$paymentId/pixQrCode", [
        'headers' => [
            'accept' => 'application/json',
            'access_token' => env('ASAAS_TOKEN'),
        ],
    ]);
    $qrData = json_decode($qrResponse->getBody(), true);
    return view('pix', [
        'paymentId' => $paymentId,
        'qr' => $qrData
    ]);
});
```

```blade
<h2>Pagamento via PIX</h2>

<p><strong>ID do pagamento:</strong> {{ $paymentId }}</p>

<img style="max-width:300px"
     src="data:image/png;base64,{{ $qr['encodedImage'] }}">

@if(isset($qr['payload']))
<p>PIX copia e cola</p>

<textarea rows="5" cols="50">
{{ $qr['payload'] }}
</textarea>
@endif
```

### Consultando o ID da Transação
```
Route::get('/verificar/{id}', function ($id) {
    $client = new Client();
    try {
        $response = $client->get("https://api.asaas.com/v3/payments/$id", [
            'headers' => [
                'accept' => 'application/json',
                'access_token' => env('ASAAS_TOKEN'),
            ],
        ]);
        $data = json_decode($response->getBody(), true);
        return response()->json([
            'status' => $data['status'],
            'valor' => $data['value'],
            'descricao' => $data['description'],
            'id' => $data['id']
        ]);

    } catch (\GuzzleHttp\Exception\ClientException $e) {
        return response()->json([
            'erro' => json_decode($e->getResponse()->getBody(), true)
        ], 400);
    }
}); 
```
#### Resposta da API
- Pagamento Recebido
```json
    {
        "status":"RECEIVED",
        "valor":5,
        "descricao":"Pagamento Pix",
        "id":"pay_elsyqaagascbht8w"
    }
```
- Pagamento não Recebido
```json
    {
      "status":"PENDING",
      "valor":5,
      "descricao":"Pagamento Pix"
      ,"id":"pay_elsyqaagascbht8w"
  }
```

### Consultando o customer do Cliente

    "customer" => "cus_0007898785621351",
    
```php
Route::get('/verificarid', function() {
    $client = new Client();
    $response = $client->post('https://api.asaas.com/v3/customers', [
        'headers' => [
            'accept' => 'application/json',
            'access_token' => env('ASAAS_TOKEN'),
            'content-type' => 'application/json',
        ],
        'json' => [
            "name" => " Nome ",
            "cpfCnpj" => " CPF ",
            "email" => " Email "
        ]
    ]);
    $customer = json_decode($response->getBody(), true);
    dd($customer);
});
```
