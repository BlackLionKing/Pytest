from jsonschema import validate
import requests
import pytest


def set_up():
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    test_json = {'kw': 'mustache'}
    # 发送json
    response = requests.post(url, data=test_json, headers=headers, verify=False)

    schema_data = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "errno": 0,
            "data": [
                {
                    "k": "mustache",
                    "v": "n. 胡子; 髭; 须状物; （哺乳动物的）触须"
                },
                {
                    "k": "mustaches",
                    "v": "n. 髭; 胡子( mustache的名词复数 ); 须状物; （哺乳动物的）触须"
                }
            ]
        }
    ],
    "required": [
        "errno",
        "data"
    ],
    "properties": {
        "errno": {
            "$id": "#/properties/errno",
            "type": "integer",
            "title": "The errno schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                0
            ]
        },
        "data": {
            "$id": "#/properties/data",
            "type": "array",
            "title": "The data schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    {
                        "k": "mustache",
                        "v": "n. 胡子; 髭; 须状物; （哺乳动物的）触须"
                    },
                    {
                        "k": "mustaches",
                        "v": "n. 髭; 胡子( mustache的名词复数 ); 须状物; （哺乳动物的）触须"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "$id": "#/properties/data/items",
                "anyOf": [
                    {
                        "$id": "#/properties/data/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "k": "mustache",
                                "v": "n. 胡子; 髭; 须状物; （哺乳动物的）触须"
                            }
                        ],
                        "required": [
                            "k",
                            "v"
                        ],
                        "properties": {
                            "k": {
                                "$id": "#/properties/data/items/anyOf/0/properties/k",
                                "type": "string",
                                "title": "The k schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "mustache"
                                ]
                            },
                            "v": {
                                "$id": "#/properties/data/items/anyOf/0/properties/v",
                                "type": "string",
                                "title": "The v schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "n. 胡子; 髭; 须状物; （哺乳动物的）触须"
                                ]
                            }
                        },
                        "additionalProperties": True
                    }
                ]
            }
        }
    },
    "additionalProperties": True
}

    json_data = {
        "errno": 0,
        "data": [
            {
                "k": "哈哈哈哈哈哈",
                "v": "哈哈哈哈"
            }]
    }
    validate(json_data, schema=schema_data)


if __name__ == '__main__':
    # pytest.main(['-v', '-s'])
    set_up()
