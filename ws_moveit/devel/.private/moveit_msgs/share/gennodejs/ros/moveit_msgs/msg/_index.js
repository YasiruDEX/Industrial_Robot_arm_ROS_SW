
"use strict";

let MoveGroupActionResult = require('./MoveGroupActionResult.js');
let ExecuteTrajectoryActionFeedback = require('./ExecuteTrajectoryActionFeedback.js');
let PickupGoal = require('./PickupGoal.js');
let MoveGroupActionFeedback = require('./MoveGroupActionFeedback.js');
let PickupActionGoal = require('./PickupActionGoal.js');
let ExecuteTrajectoryResult = require('./ExecuteTrajectoryResult.js');
let PlaceResult = require('./PlaceResult.js');
let MoveGroupActionGoal = require('./MoveGroupActionGoal.js');
let MoveGroupSequenceFeedback = require('./MoveGroupSequenceFeedback.js');
let MoveGroupAction = require('./MoveGroupAction.js');
let MoveGroupFeedback = require('./MoveGroupFeedback.js');
let MoveGroupSequenceResult = require('./MoveGroupSequenceResult.js');
let PlaceFeedback = require('./PlaceFeedback.js');
let PickupAction = require('./PickupAction.js');
let PlaceActionGoal = require('./PlaceActionGoal.js');
let ExecuteTrajectoryActionGoal = require('./ExecuteTrajectoryActionGoal.js');
let PickupFeedback = require('./PickupFeedback.js');
let ExecuteTrajectoryAction = require('./ExecuteTrajectoryAction.js');
let MoveGroupSequenceActionFeedback = require('./MoveGroupSequenceActionFeedback.js');
let ExecuteTrajectoryFeedback = require('./ExecuteTrajectoryFeedback.js');
let PlaceGoal = require('./PlaceGoal.js');
let PickupResult = require('./PickupResult.js');
let MoveGroupSequenceGoal = require('./MoveGroupSequenceGoal.js');
let ExecuteTrajectoryGoal = require('./ExecuteTrajectoryGoal.js');
let PlaceAction = require('./PlaceAction.js');
let PlaceActionFeedback = require('./PlaceActionFeedback.js');
let MoveGroupSequenceAction = require('./MoveGroupSequenceAction.js');
let PickupActionResult = require('./PickupActionResult.js');
let MoveGroupResult = require('./MoveGroupResult.js');
let MoveGroupGoal = require('./MoveGroupGoal.js');
let PickupActionFeedback = require('./PickupActionFeedback.js');
let MoveGroupSequenceActionGoal = require('./MoveGroupSequenceActionGoal.js');
let MoveGroupSequenceActionResult = require('./MoveGroupSequenceActionResult.js');
let PlaceActionResult = require('./PlaceActionResult.js');
let ExecuteTrajectoryActionResult = require('./ExecuteTrajectoryActionResult.js');
let MotionPlanResponse = require('./MotionPlanResponse.js');
let MotionSequenceItem = require('./MotionSequenceItem.js');
let RobotState = require('./RobotState.js');
let AttachedCollisionObject = require('./AttachedCollisionObject.js');
let CartesianTrajectory = require('./CartesianTrajectory.js');
let PlanningOptions = require('./PlanningOptions.js');
let ObjectColor = require('./ObjectColor.js');
let LinkScale = require('./LinkScale.js');
let BoundingVolume = require('./BoundingVolume.js');
let CartesianPoint = require('./CartesianPoint.js');
let PlanningSceneComponents = require('./PlanningSceneComponents.js');
let MotionPlanRequest = require('./MotionPlanRequest.js');
let PositionIKRequest = require('./PositionIKRequest.js');
let MoveItErrorCodes = require('./MoveItErrorCodes.js');
let PlanningScene = require('./PlanningScene.js');
let AllowedCollisionMatrix = require('./AllowedCollisionMatrix.js');
let TrajectoryConstraints = require('./TrajectoryConstraints.js');
let VisibilityConstraint = require('./VisibilityConstraint.js');
let GenericTrajectory = require('./GenericTrajectory.js');
let PlaceLocation = require('./PlaceLocation.js');
let RobotTrajectory = require('./RobotTrajectory.js');
let PositionConstraint = require('./PositionConstraint.js');
let PlannerInterfaceDescription = require('./PlannerInterfaceDescription.js');
let JointLimits = require('./JointLimits.js');
let KinematicSolverInfo = require('./KinematicSolverInfo.js');
let MotionPlanDetailedResponse = require('./MotionPlanDetailedResponse.js');
let OrientationConstraint = require('./OrientationConstraint.js');
let DisplayTrajectory = require('./DisplayTrajectory.js');
let CartesianTrajectoryPoint = require('./CartesianTrajectoryPoint.js');
let Grasp = require('./Grasp.js');
let DisplayRobotState = require('./DisplayRobotState.js');
let JointConstraint = require('./JointConstraint.js');
let PlanningSceneWorld = require('./PlanningSceneWorld.js');
let MotionSequenceRequest = require('./MotionSequenceRequest.js');
let OrientedBoundingBox = require('./OrientedBoundingBox.js');
let CollisionObject = require('./CollisionObject.js');
let Constraints = require('./Constraints.js');
let PlannerParams = require('./PlannerParams.js');
let GripperTranslation = require('./GripperTranslation.js');
let ContactInformation = require('./ContactInformation.js');
let ConstraintEvalResult = require('./ConstraintEvalResult.js');
let MotionSequenceResponse = require('./MotionSequenceResponse.js');
let CostSource = require('./CostSource.js');
let LinkPadding = require('./LinkPadding.js');
let WorkspaceParameters = require('./WorkspaceParameters.js');
let AllowedCollisionEntry = require('./AllowedCollisionEntry.js');

module.exports = {
  MoveGroupActionResult: MoveGroupActionResult,
  ExecuteTrajectoryActionFeedback: ExecuteTrajectoryActionFeedback,
  PickupGoal: PickupGoal,
  MoveGroupActionFeedback: MoveGroupActionFeedback,
  PickupActionGoal: PickupActionGoal,
  ExecuteTrajectoryResult: ExecuteTrajectoryResult,
  PlaceResult: PlaceResult,
  MoveGroupActionGoal: MoveGroupActionGoal,
  MoveGroupSequenceFeedback: MoveGroupSequenceFeedback,
  MoveGroupAction: MoveGroupAction,
  MoveGroupFeedback: MoveGroupFeedback,
  MoveGroupSequenceResult: MoveGroupSequenceResult,
  PlaceFeedback: PlaceFeedback,
  PickupAction: PickupAction,
  PlaceActionGoal: PlaceActionGoal,
  ExecuteTrajectoryActionGoal: ExecuteTrajectoryActionGoal,
  PickupFeedback: PickupFeedback,
  ExecuteTrajectoryAction: ExecuteTrajectoryAction,
  MoveGroupSequenceActionFeedback: MoveGroupSequenceActionFeedback,
  ExecuteTrajectoryFeedback: ExecuteTrajectoryFeedback,
  PlaceGoal: PlaceGoal,
  PickupResult: PickupResult,
  MoveGroupSequenceGoal: MoveGroupSequenceGoal,
  ExecuteTrajectoryGoal: ExecuteTrajectoryGoal,
  PlaceAction: PlaceAction,
  PlaceActionFeedback: PlaceActionFeedback,
  MoveGroupSequenceAction: MoveGroupSequenceAction,
  PickupActionResult: PickupActionResult,
  MoveGroupResult: MoveGroupResult,
  MoveGroupGoal: MoveGroupGoal,
  PickupActionFeedback: PickupActionFeedback,
  MoveGroupSequenceActionGoal: MoveGroupSequenceActionGoal,
  MoveGroupSequenceActionResult: MoveGroupSequenceActionResult,
  PlaceActionResult: PlaceActionResult,
  ExecuteTrajectoryActionResult: ExecuteTrajectoryActionResult,
  MotionPlanResponse: MotionPlanResponse,
  MotionSequenceItem: MotionSequenceItem,
  RobotState: RobotState,
  AttachedCollisionObject: AttachedCollisionObject,
  CartesianTrajectory: CartesianTrajectory,
  PlanningOptions: PlanningOptions,
  ObjectColor: ObjectColor,
  LinkScale: LinkScale,
  BoundingVolume: BoundingVolume,
  CartesianPoint: CartesianPoint,
  PlanningSceneComponents: PlanningSceneComponents,
  MotionPlanRequest: MotionPlanRequest,
  PositionIKRequest: PositionIKRequest,
  MoveItErrorCodes: MoveItErrorCodes,
  PlanningScene: PlanningScene,
  AllowedCollisionMatrix: AllowedCollisionMatrix,
  TrajectoryConstraints: TrajectoryConstraints,
  VisibilityConstraint: VisibilityConstraint,
  GenericTrajectory: GenericTrajectory,
  PlaceLocation: PlaceLocation,
  RobotTrajectory: RobotTrajectory,
  PositionConstraint: PositionConstraint,
  PlannerInterfaceDescription: PlannerInterfaceDescription,
  JointLimits: JointLimits,
  KinematicSolverInfo: KinematicSolverInfo,
  MotionPlanDetailedResponse: MotionPlanDetailedResponse,
  OrientationConstraint: OrientationConstraint,
  DisplayTrajectory: DisplayTrajectory,
  CartesianTrajectoryPoint: CartesianTrajectoryPoint,
  Grasp: Grasp,
  DisplayRobotState: DisplayRobotState,
  JointConstraint: JointConstraint,
  PlanningSceneWorld: PlanningSceneWorld,
  MotionSequenceRequest: MotionSequenceRequest,
  OrientedBoundingBox: OrientedBoundingBox,
  CollisionObject: CollisionObject,
  Constraints: Constraints,
  PlannerParams: PlannerParams,
  GripperTranslation: GripperTranslation,
  ContactInformation: ContactInformation,
  ConstraintEvalResult: ConstraintEvalResult,
  MotionSequenceResponse: MotionSequenceResponse,
  CostSource: CostSource,
  LinkPadding: LinkPadding,
  WorkspaceParameters: WorkspaceParameters,
  AllowedCollisionEntry: AllowedCollisionEntry,
};
