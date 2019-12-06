#!/usr/bin/env python

import flowrisk as fr


class Config(fr.BulkConfVPINConfig):

    TIME_BAR_VOLUME_COL_NAME = 'volume'
    
    BUCKET_MAX_VOLUME = 500
    N_TIME_BAR_FOR_INITIALIZATION = 50

    N_BUCKET_OR_BUCKET_DECAY = 0.95
    BUCKETS = fr.bulk.RecursiveBulkClassEWMABuckets


if __name__ == '__main__':
    config = Config()
    config.summary()
    example = fr.examples.Coins(config)

    symbols = example.list_symbols()
    for symbol in symbols:
        result = example.estimate_vpin_and_conf_interval(symbol)
        example.draw_price_vpins_and_conf_intervals()
