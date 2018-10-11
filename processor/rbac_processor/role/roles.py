# Copyright 2018 Contributors to Hyperledger Sawtooth
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

from rbac_processor.protobuf import role_transaction_pb2
from rbac_processor.role import role_validator
from rbac_processor import state_change


def new_role(payload, state):
    create_role = role_transaction_pb2.CreateRole()
    create_role.ParseFromString(payload.content)

    role_validator.validate_create_role_payload(create_role)
    role_validator.validate_create_role_state(create_role, state)
    state_change.create_role(create_role, state)