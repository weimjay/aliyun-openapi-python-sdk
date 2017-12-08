# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeRouteTableListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'DescribeRouteTableList','vpc')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_Bandwidth(self):
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self,Bandwidth):
		self.add_query_param('Bandwidth',Bandwidth)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_RouterType(self):
		return self.get_query_params().get('RouterType')

	def set_RouterType(self,RouterType):
		self.add_query_param('RouterType',RouterType)

	def get_KbpsBandwidth(self):
		return self.get_query_params().get('KbpsBandwidth')

	def set_KbpsBandwidth(self,KbpsBandwidth):
		self.add_query_param('KbpsBandwidth',KbpsBandwidth)

	def get_RouteTableName(self):
		return self.get_query_params().get('RouteTableName')

	def set_RouteTableName(self,RouteTableName):
		self.add_query_param('RouteTableName',RouteTableName)

	def get_RouterId(self):
		return self.get_query_params().get('RouterId')

	def set_RouterId(self,RouterId):
		self.add_query_param('RouterId',RouterId)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_ResourceUid(self):
		return self.get_query_params().get('ResourceUid')

	def set_ResourceUid(self,ResourceUid):
		self.add_query_param('ResourceUid',ResourceUid)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ResourceBid(self):
		return self.get_query_params().get('ResourceBid')

	def set_ResourceBid(self,ResourceBid):
		self.add_query_param('ResourceBid',ResourceBid)

	def get_RouteTableId(self):
		return self.get_query_params().get('RouteTableId')

	def set_RouteTableId(self,RouteTableId):
		self.add_query_param('RouteTableId',RouteTableId)