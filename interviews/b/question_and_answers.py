"""
Given a list of questions and their answers with rating, create a new list with unique questions based on their content,
ordered by questions ids. Keep question with best answer. When both questions have exactly
rated answer we keep older question. How would you make sure that your code works?

Sample input
[{
    "id": 123,
    "content": "Test content",
    "createTimestamp": 123213,
    "answers": [{
        "id": 142,
        "rating": 10,
        "content": "Test answer"
    }, {
        "id": 242,
        "rating": 2,
        "content": "Test answer 2"
    }]
}, {
    "id": 1024,
    "content": "Test content",
    "createTimestamp": 54343,
    "answers": [{
        "id": 454,
        "rating": 9,
        "content": "Test answer 2"
    }, {
        "id": 342,
        "rating": 4,
        "content": "Test answer 3"
    }]
},
{
    "id": 250,
    "content": "Different test content",
    "createTimestamp": 543431,
    "answers": [{
        "id": 854,
        "rating": 10,
        "content": "Test answer 4"
    }, {
        "id": 346,
        "rating": 3,
        "content": "Test answer 5"
    }]
}]


Sample output
[{
    "id": 123,
    "content": "Test content",
    "createTimestamp": 123213,
    "answers": [{
        "id": 142,
        "rating": 10,
        "content": "Test answer"
    }, {
        "id": 242,
        "rating": 2,
        "content": "Test answer 2"
    }]
},
{
    "id": 250,
    "content": "Different test content",
    "createTimestamp": 543431,
    "answers": [{
        "id": 854,
        "rating": 10,
        "content": "Test answer 4"
    }, {
        "id": 346,
        "rating": 3,
        "content": "Test answer 5"
    }]
}]
"""