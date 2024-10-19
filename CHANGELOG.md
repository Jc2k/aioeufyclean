# CHANGELOG



## v0.4.0 (2024-10-19)

### Chore

* chore: add script that shows usage ([`51a35af`](https://github.com/Jc2k/aioeufyclean/commit/51a35affb51c29869cd77a58a12a7932ad722f94))

### Feature

* feat: can now get model_id ([`b66b371`](https://github.com/Jc2k/aioeufyclean/commit/b66b371019897854b7432cf0fd96283079b26307))

* feat: clean_speed_list is now correct based on model id ([`97a80d2`](https://github.com/Jc2k/aioeufyclean/commit/97a80d205e78a45a94001cb7b82b67140b88d9d5))


## v0.3.1 (2024-10-18)

### Fix

* fix: improve stability after ping refactor ([`d0ff3b2`](https://github.com/Jc2k/aioeufyclean/commit/d0ff3b2c5a848b1d292f249cf38f238fec050f08))


## v0.3.0 (2024-10-18)

### Chore

* chore: start refactoring ping into main event loop ([`75b94bd`](https://github.com/Jc2k/aioeufyclean/commit/75b94bd3c6a6d42b0fa736d53af47dc93114049f))

### Feature

* feat: support switches, towards a background task for use with config_entry.async_create_background_task ([`16ad90f`](https://github.com/Jc2k/aioeufyclean/commit/16ad90fc18134b99b4cc7265273813740d2971b8))


## v0.2.0 (2024-10-17)

### Chore

* chore: remove unused logging ([`5898e9a`](https://github.com/Jc2k/aioeufyclean/commit/5898e9aca2a56a18dac8063ec4423f08be1707d0))

* chore: more clean up ([`c859d44`](https://github.com/Jc2k/aioeufyclean/commit/c859d4498e442473a8986b7504e5f8ea8f5ff9c6))

* chore: remove unused code ([`9bc149a`](https://github.com/Jc2k/aioeufyclean/commit/9bc149a4b1eec7da7d86a9d085fdf73cc5633b5b))

* chore: more README updates ([`6f3613d`](https://github.com/Jc2k/aioeufyclean/commit/6f3613da1d9ce2dd3fe95763d443a3874e7068f5))

* chore: tweak README ([`b708d1e`](https://github.com/Jc2k/aioeufyclean/commit/b708d1ec7317ab5bdbee273180db1776156d7936))

### Feature

* feat: async_add_availability_callback ([`19c5856`](https://github.com/Jc2k/aioeufyclean/commit/19c5856c0989640783d03a3f22982d510b9a985a))

* feat: async_add_state_callback ([`6d64385`](https://github.com/Jc2k/aioeufyclean/commit/6d64385a39b863e2e32e9c9b5a2500e2f19e67e5))

* feat: add spot clean ([`cf821d7`](https://github.com/Jc2k/aioeufyclean/commit/cf821d7209d248436b175696c6810200c725a547))

### Fix

* fix: incorrect isort configuration ([`1746be8`](https://github.com/Jc2k/aioeufyclean/commit/1746be800de83e09893f931befdb557b7b40cd72))


## v0.1.0 (2024-10-17)

### Chore

* chore: more lint fixes ([`7567665`](https://github.com/Jc2k/aioeufyclean/commit/7567665236891962274ad81ad1bbdd355c09daff))

* chore: fix mypy ([`5b93cfd`](https://github.com/Jc2k/aioeufyclean/commit/5b93cfdba0e468ee132fbaf9fa78e5c90593d179))

* chore: remove unused code ([`b2c423a`](https://github.com/Jc2k/aioeufyclean/commit/b2c423a078a5ae96430a14eac48d107b918d9d02))

* chore: refactoring ([`67e5182`](https://github.com/Jc2k/aioeufyclean/commit/67e5182d192f3ff147b3ec1434847324840b235a))

* chore: update gitignore ([`af44869`](https://github.com/Jc2k/aioeufyclean/commit/af448696b384393db3155b8d3ad6b8db4b2f43b2))

* chore: more cleanup ([`a31eccd`](https://github.com/Jc2k/aioeufyclean/commit/a31eccd83aec16beb8564b068724cc1c107dfc67))

* chore: fix extracting device access key ([`1925c43`](https://github.com/Jc2k/aioeufyclean/commit/1925c435d9bbacfbe3acde825b46e79fdd5c1fc2))

* chore: ruff fmt ([`8eba4b0`](https://github.com/Jc2k/aioeufyclean/commit/8eba4b02eecaa7b6728b3255920fa7d9d92e3570))

* chore: adding more typing ([`1d554e5`](https://github.com/Jc2k/aioeufyclean/commit/1d554e57f027a599f8e6abc8e46c60dad437d3bb))

* chore: add stub readme ([`24876ef`](https://github.com/Jc2k/aioeufyclean/commit/24876ef61e50e37c67e9d3b46b47b39bcc0b40cb))

* chore: add py.typed marker file ([`993d766`](https://github.com/Jc2k/aioeufyclean/commit/993d76616d97e0908b393e4c7abaeacb7f8d38a0))

* chore: non blocking connect ([`69949be`](https://github.com/Jc2k/aioeufyclean/commit/69949be183fea5d88c44db74c88e536b2c5b3cb3))

* chore: get rid of _call_async ([`b346abc`](https://github.com/Jc2k/aioeufyclean/commit/b346abc048b1386ca18239a854baa6c5cc1290e9))

* chore: get rid of callback in device.py ([`32d71c8`](https://github.com/Jc2k/aioeufyclean/commit/32d71c8dce18215842b78af3ab2e008354f2d626))

* chore: use StrEnum from stdlib ([`e987dc9`](https://github.com/Jc2k/aioeufyclean/commit/e987dc9a9c8ece8d79389591f552512ed623930e))

* chore: fix ruff lints ([`e0fed7f`](https://github.com/Jc2k/aioeufyclean/commit/e0fed7fcae4a474b99052c405d286a94b8bc7567))

* chore: ruff fmt ([`9dd80b3`](https://github.com/Jc2k/aioeufyclean/commit/9dd80b39e94376667fca5471553c2c28f5eb5080))

* chore: ruff fix ([`5dfe993`](https://github.com/Jc2k/aioeufyclean/commit/5dfe993a066ca2118f025ae8f90f00ae62af8f66))

* chore: uv sync ([`0f25627`](https://github.com/Jc2k/aioeufyclean/commit/0f25627d20138b5f9d1bfc3a4f67d349a8b9efb2))

* chore: project skaffolding ([`fe4b90b`](https://github.com/Jc2k/aioeufyclean/commit/fe4b90b16d30bd87b4e8d07283a3f8fe31d92860))

### Feature

* feat: work towards extracting access token for local control ([`25bfa5e`](https://github.com/Jc2k/aioeufyclean/commit/25bfa5efa537ab62d167075f79cec49efd6e9395))

* feat: start logging in ([`2e993be`](https://github.com/Jc2k/aioeufyclean/commit/2e993bede93e18d89aef7cac9dc2a3e25ba3dd05))

* feat: lock around connect to avoid parallel connection attempts ([`2324906`](https://github.com/Jc2k/aioeufyclean/commit/232490639928d4b23cf9ae138a28d8381eb6ff23))

* feat: add initial device wrapper (thanks mitch) ([`07e4d3c`](https://github.com/Jc2k/aioeufyclean/commit/07e4d3c54fdd3389b6b7af1ebca1473220be261a))
