# Nexus Hello

An example project for Nexus framework, that is also used in Nexus integration tests. Supported features:
- :white_check_mark: `MinimalisticAlgorithm`
- :white_check_mark: Interaction with Nexus Receiver
- :white_check_mark: Payload parsing

In progress:
- [ ] `ForkedAlgorithm`
- [ ] `DistributedAlgorithm`
- [ ] `Data readers and processors`
- [ ] `UserTelemetry` classes

## Usage

You can run the algorithm with the following command:
```shell
python -m main.py --sas-uri https://my-payload-location --request-id "c13e2f71-f196-4e2e-8427-5a2a8e269e42"
```
