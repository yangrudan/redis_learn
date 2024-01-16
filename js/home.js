const Redis = require('ioredis');

const redis = new Redis(6379, '127.0.0.1');

redis.set('foo', 'bar', function(){
    redis.get('foo', function(err, result){
        console.log(result);
    })
});

