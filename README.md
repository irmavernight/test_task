# Test task

### Request
```
POST http://localhost:5000/
```

```
Content-type: application/json
```

| Field | Type | Description |
| ----------- | ------------| ----------- |
| loan  | int | Loan amount  |
| period_month | int | Period in month  |
| interest | float | Annual interest | 

### Response
```
{
    "cumulative_interest": 287478.42
}
```
